using Microsoft.Extensions.Caching.Memory;
using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Models;

namespace PrintableFormsWordAddIn.Application.Services
{
    public class MemoryCacheService : IMemoryCacheService
    {
        private IMemoryCache memoryCache;

        public MemoryCacheService()
        {
            var options = new MemoryCacheOptions()
            {

            };

            memoryCache = new MemoryCache(options);
        }

        public void CacheToken(KeyCloakToken token)
        {
            memoryCache.Set("token", token);
        }

        public KeyCloakToken GetToken()
        {
            if(memoryCache.TryGetValue("token", out KeyCloakToken token))
                return token;
            else
                return null;
        }
    }
}
