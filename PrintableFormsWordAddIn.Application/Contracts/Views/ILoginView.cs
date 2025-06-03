using PrintableFormsWordAddIn.Application.Utils;

namespace PrintableFormsWordAddIn.Application.Contracts.Views
{
    public interface ILoginView
    {
        string Username { get; }
        string Password { get; }
        event AsyncEventHandler Login;
        void ShowSuccess();
        void ShowError(string message);
    }
}
