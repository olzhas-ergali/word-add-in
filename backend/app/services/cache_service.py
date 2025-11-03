from cachetools import TTLCache
from typing import Optional, Any
from app.config import settings
from app.models.keycloak import KeyCloakToken


class CacheService:
    """Simple in-memory cache service with TTL"""
    
    def __init__(self, maxsize: int = 100, ttl: int = None):
        """
        Initialize cache service
        
        Args:
            maxsize: Maximum number of cached items
            ttl: Time to live in seconds (default from settings)
        """
        self.ttl = ttl or settings.cache_ttl
        self._cache = TTLCache(maxsize=maxsize, ttl=self.ttl)
    
    def cache_token(self, session_id: str, token: KeyCloakToken) -> None:
        """
        Cache authentication token
        
        Args:
            session_id: Unique session identifier
            token: KeyCloak token to cache
        """
        self._cache[f"token:{session_id}"] = token
    
    def get_token(self, session_id: str) -> Optional[KeyCloakToken]:
        """
        Retrieve cached token
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            Cached token or None if not found/expired
        """
        return self._cache.get(f"token:{session_id}")
    
    def remove_token(self, session_id: str) -> None:
        """
        Remove cached token
        
        Args:
            session_id: Unique session identifier
        """
        key = f"token:{session_id}"
        if key in self._cache:
            del self._cache[key]
    
    def set(self, key: str, value: Any) -> None:
        """
        Set generic cache value
        
        Args:
            key: Cache key
            value: Value to cache
        """
        self._cache[key] = value
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get generic cache value
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None
        """
        return self._cache.get(key)
    
    def delete(self, key: str) -> None:
        """
        Delete cache entry
        
        Args:
            key: Cache key
        """
        if key in self._cache:
            del self._cache[key]
    
    def clear(self) -> None:
        """Clear all cache entries"""
        self._cache.clear()


# Global cache instance
cache_service = CacheService()

