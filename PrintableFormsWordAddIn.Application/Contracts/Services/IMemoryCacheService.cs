using PrintableFormsWordAddIn.Application.Models;

namespace PrintableFormsWordAddIn.Application.Contracts.Services
{
    public interface IMemoryCacheService
    {
        void CacheToken(KeyCloakToken token);
        KeyCloakToken GetToken();
    }
}
