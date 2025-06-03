using Newtonsoft.Json;
using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Models;
using System.Collections.Generic;
using System.Configuration;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Application.Services
{
    public class KeyCloakService : IKeyCloakService
    {
        public KeyCloakService() 
        {

        }

        public async Task<KeyCloakResponse> ValidateUser(string username, string password)
        {
            var clientApi = ConfigurationManager.AppSettings["KeyCloakClientApi"];
            var clientId = ConfigurationManager.AppSettings["KeyCloakClientId"];
            var clientSecret = ConfigurationManager.AppSettings["KeyCloakClientSecret"];

            var body = new Dictionary<string, string>
            {
                { "grant_type", "password" },
                { "scope", "openid" },
                { "username", username },
                { "password", password },
                { "client_id", clientId },
                { "client_secret", clientSecret }
            };

            var request = new HttpRequestMessage(HttpMethod.Post, clientApi);
            request.Content = new FormUrlEncodedContent(body);

            var response = await SendPostRequest(request);
            return await ProcessResponse(response);
        }

        private async Task<HttpResponseMessage> SendPostRequest(HttpRequestMessage request)
        {
            using (var client = new HttpClient())
            {
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3
                                                    | SecurityProtocolType.Tls
                                                    | SecurityProtocolType.Tls11
                                                    | SecurityProtocolType.Tls12;

                return await client.SendAsync(request);
            }
        }

        private async Task<KeyCloakResponse> ProcessResponse(HttpResponseMessage responseMessage)
        {
            var responseContent = await responseMessage.Content.ReadAsStringAsync();

            var response = new KeyCloakResponse();
            response.Status = responseMessage.StatusCode;
            response.Success = responseMessage.IsSuccessStatusCode;

            if (responseMessage.StatusCode >= System.Net.HttpStatusCode.BadRequest)
            {
                if ((int)responseMessage.StatusCode >= 500)
                {
                    throw new HttpRequestException(responseContent);
                }

                var keyCloakError = JsonConvert.DeserializeObject<KeyCloakError>(responseContent);
                response.Error = keyCloakError.Error;
                response.ErrorDescription = keyCloakError.ErrorDescription;
            }
            else
            {
                response.Data = JsonConvert.DeserializeObject<KeyCloakToken>(responseContent);
            }

            return response;
        }
    }
}
