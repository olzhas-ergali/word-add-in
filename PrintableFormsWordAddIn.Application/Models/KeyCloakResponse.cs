using System.Collections.Generic;
using System.Net;

namespace PrintableFormsWordAddIn.Application.Models
{
    public class KeyCloakResponse
    {
        public KeyCloakToken Data { get; set; }
        public string Error { get; set; }
        public string ErrorDescription { get; set; }
        public string Message => GetMessage(Error, ErrorDescription);
        public bool Success { get; set; }
        public HttpStatusCode Status { get; set; }

        public KeyCloakResponse()
        {

        }

        public KeyCloakResponse(string error, string errorDescription, bool success, HttpStatusCode status)
        {
            Error = error;
            ErrorDescription = errorDescription;
            Success = success;
            Status = status;
        }

        public string GetMessage(string error, string errorDescription)
        {
            var data = new Dictionary<(string, string), string>
            {
                { ("invalid_grant", "Invalid user credentials"), "Неверный логин или пароль." },
                { ("invalid_grant", "Token is not active"), "Токен не активен." },
                { ("invalid_grant", "Invalid refresh token"), "Недействительный рефреш токен." },
                { ("invalid_grant", "Session not active"), "Сессия пользователя не активна." },
                { ("invalid_grant", "Code not valid"), "Недействительный код." },
                { ("invalid_grant", "Stale token"), "Устаревший токен." },
                { ("invalid_request", "Missing form parameter"), "Отсутствует один или несколько параметров атрибута 'form' запроса." },
                { ("invalid_request", "Missing parameter"), "Отсутствует один или несколько параметров запроса." },
                { ("invalid_request", "No refresh token"), "Рефреш не возвращен и сессия пользователя не создана." },
                { ("unauthorized_client", "Invalid client credentials"), "Неверный логин или пароль клиента." },
                { ("unauthorized_client", "Invalid client secret"), "Невалидный секрет клиента." },
                { ("unauthorized_client", "Client secret not provided in request"), "Секрет клиента не был предоставлен в запросе." },
                { ("unsupported_grant_type", "Unsupported grant_type"), "Неподдерживаемый тип гранта." },
                { ("response-deserialization-failed", "response-deserialization-failed"), "Произошла ошибка во время десериализации." },
                { ("invalid_scope", null), "Невалидный scope." },
                { ("Could not find role", null), "Не найдена роль." },
                { ("User not found", null), "Учетная запись не найдена." },
                { (null, "Invalid email address."), "Неверный адрес электронной почты." },
            };

            if (data.TryGetValue((error, errorDescription), out string value))
                return value;
            else
                return Success ? null : error + " " + errorDescription;
        }
    }
}
