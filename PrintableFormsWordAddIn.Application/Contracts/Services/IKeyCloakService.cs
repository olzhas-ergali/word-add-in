using PrintableFormsWordAddIn.Application.Models;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Application.Contracts.Services
{
    public interface IKeyCloakService
    {
        Task<KeyCloakResponse> ValidateUser(string username, string password);
    }
}
