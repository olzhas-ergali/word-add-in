using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Contracts.Views;
using PrintableFormsWordAddIn.Application.Services;
using System;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Presenters
{
    public class LoginPresenter
    {
        private readonly ILoginView loginView;
        private readonly IKeyCloakService keyCloakService;

        public LoginPresenter(ILoginView loginView)
        {
            this.loginView = loginView;
            this.loginView.Login += OnLogin;
            this.keyCloakService = new KeyCloakService();
        }

        private async Task OnLogin(object sender, EventArgs e)
        {
            var response = await keyCloakService.ValidateUser(loginView.Username, loginView.Password);

            if (response.Success)
            {
                Globals.ThisAddIn.MemoryCacheService.CacheToken(response.Data);
                loginView.ShowSuccess();
            }
            else
            {
                loginView.ShowError(response.Message);
            }
        }
    }
}
