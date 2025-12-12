"""Tests for Airflow version detection."""

import pytest

from astro_airflow_mcp.version_detection import (
    VersionCache,
    detect_airflow_version,
    get_or_detect_version,
)


class TestVersionDetection:
    """Tests for Airflow version detection."""

    def test_detect_version_2(self, mocker):
        """Test detection of Airflow 2.x."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "2.9.0"}
        mock_response.raise_for_status = mocker.Mock()

        mocker.patch("httpx.get", return_value=mock_response)

        major, full = detect_airflow_version("http://localhost:8080")
        assert major == 2
        assert full == "2.9.0"

    def test_detect_version_3(self, mocker):
        """Test detection of Airflow 3.x."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "3.1.3"}
        mock_response.raise_for_status = mocker.Mock()

        mocker.patch("httpx.get", return_value=mock_response)

        major, full = detect_airflow_version("http://localhost:8080")
        assert major == 3
        assert full == "3.1.3"

    def test_detect_unsupported_version(self, mocker):
        """Test error handling for unsupported versions."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "1.10.0"}
        mock_response.raise_for_status = mocker.Mock()

        mocker.patch("httpx.get", return_value=mock_response)

        with pytest.raises(RuntimeError, match="Unsupported Airflow version"):
            detect_airflow_version("http://localhost:8080")

    def test_detect_invalid_version_string(self, mocker):
        """Test error handling for invalid version strings."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "invalid"}
        mock_response.raise_for_status = mocker.Mock()

        mocker.patch("httpx.get", return_value=mock_response)

        with pytest.raises(RuntimeError, match="Error parsing Airflow version"):
            detect_airflow_version("http://localhost:8080")

    def test_detect_empty_version(self, mocker):
        """Test error handling for empty version."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": ""}
        mock_response.raise_for_status = mocker.Mock()

        mocker.patch("httpx.get", return_value=mock_response)

        with pytest.raises(RuntimeError, match="Version string empty"):
            detect_airflow_version("http://localhost:8080")

    def test_detect_with_auth_token(self, mocker):
        """Test version detection with authentication token."""
        mock_response = mocker.Mock()
        mock_response.json.return_value = {"version": "3.1.3"}
        mock_response.raise_for_status = mocker.Mock()

        mock_get = mocker.patch("httpx.get", return_value=mock_response)

        detect_airflow_version("http://localhost:8080", auth_token="test-token")

        # Verify auth header was passed
        call_kwargs = mock_get.call_args[1]
        assert "headers" in call_kwargs
        assert call_kwargs["headers"]["Authorization"] == "Bearer test-token"


class TestVersionCache:
    """Tests for version caching mechanism."""

    def test_cache_initially_empty(self):
        """Test cache is empty on creation."""
        cache = VersionCache()
        assert cache.get() is None

    def test_cache_set_and_get(self):
        """Test caching and retrieving version."""
        cache = VersionCache()
        cache.set(2, "2.9.0")

        result = cache.get()
        assert result is not None
        assert result == (2, "2.9.0")

    def test_cache_clear(self):
        """Test clearing the cache."""
        cache = VersionCache()
        cache.set(3, "3.1.3")
        assert cache.get() is not None

        cache.clear()
        assert cache.get() is None

    def test_get_or_detect_uses_cache(self, mocker):
        """Test that get_or_detect_version uses cache when available."""
        from astro_airflow_mcp.version_detection import _version_cache

        # Clear cache first to ensure clean state
        _version_cache.clear()

        # Mock version detection
        mock_detect = mocker.patch(
            "astro_airflow_mcp.version_detection.detect_airflow_version", return_value=(3, "3.1.3")
        )

        # First call should detect
        result1 = get_or_detect_version("http://localhost:8080")
        assert result1 == (3, "3.1.3")
        assert mock_detect.call_count == 1

        # Second call should use cache
        result2 = get_or_detect_version("http://localhost:8080")
        assert result2 == (3, "3.1.3")
        assert mock_detect.call_count == 1  # Still 1, not called again

    def test_get_or_detect_after_clear(self, mocker):
        """Test that clearing cache forces re-detection."""
        from astro_airflow_mcp.version_detection import _version_cache

        # Clear cache first to ensure clean state
        _version_cache.clear()

        mock_detect = mocker.patch(
            "astro_airflow_mcp.version_detection.detect_airflow_version", return_value=(2, "2.9.0")
        )

        # First call
        get_or_detect_version("http://localhost:8080")
        assert mock_detect.call_count == 1

        # Clear cache
        _version_cache.clear()

        # Next call should detect again
        get_or_detect_version("http://localhost:8080")
        assert mock_detect.call_count == 2
