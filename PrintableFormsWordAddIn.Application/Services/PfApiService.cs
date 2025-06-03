using Newtonsoft.Json;
using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Models;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Application.Services
{
    public class PfApiService : IPfApiService
    {
        private readonly IMemoryCacheService memoryCacheService;

        public PfApiService(IMemoryCacheService memoryCacheService)
        {
            this.memoryCacheService = memoryCacheService;
        }

        public async Task<IEnumerable<DocumentVariable>> GetDocumentVariables(Guid documentId)
        {
            var getDocVariablesApi = ConfigurationManager.AppSettings["PrintableFormsBaseUrl"] + 
                ConfigurationManager.AppSettings["PrintableFormsGetDocVariablesApi"];
            var request = new HttpRequestMessage(HttpMethod.Get, getDocVariablesApi + "?documentId=" + documentId);

            var responseMessage = await SendRequest(request);

            if (responseMessage.IsSuccessStatusCode)
            {
                var responseContent = await responseMessage.Content.ReadAsStringAsync();
                return JsonConvert.DeserializeObject<List<DocumentVariable>>(responseContent);
            }

            return new List<DocumentVariable>();
        }

        public async Task<IEnumerable<DocumentVariable>> GetDocumentVariablesWithValues(IEnumerable<string> ids)
        {
            var getVariableValuesApi = ConfigurationManager.AppSettings["PrintableFormsBaseUrl"] +
                ConfigurationManager.AppSettings["PrintableFormsGetVariableValuesApi"];
            var request = new HttpRequestMessage(HttpMethod.Post, getVariableValuesApi);


            var body = "{\"ids\": [\"" + string.Join("\",\"", ids) + "\"]}";
            request.Content = new StringContent(body, Encoding.UTF8, "application/json");

            var responseMessage = new HttpResponseMessage();
            using (var client = new HttpClient())
            {
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3
                                                    | SecurityProtocolType.Tls
                                                    | SecurityProtocolType.Tls11
                                                    | SecurityProtocolType.Tls12;

                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                responseMessage = await client.SendAsync(request);
            }

            if (responseMessage.IsSuccessStatusCode)
            {
                var responseContent = await responseMessage.Content.ReadAsStringAsync();
                return JsonConvert.DeserializeObject<List<DocumentVariable>>(responseContent);
            }

            return new List<DocumentVariable>();
        }

        public async Task<Stream> GetPfDocument(Guid id)
        {
            var getDocxApi = ConfigurationManager.AppSettings["PrintableFormsBaseUrl"] +
                ConfigurationManager.AppSettings["PrintableFormsGetDocxApi"];
            var request = new HttpRequestMessage(HttpMethod.Get, getDocxApi + "?documentId=" + id);

            //var token = memoryCacheService.GetToken();

            //request.Headers.Add("Authorization", "Bearer " + token.AccessToken);

            var responseMessage = await SendRequest(request);

            if (responseMessage.IsSuccessStatusCode)
            {
                return await responseMessage.Content.ReadAsStreamAsync();
            }

            return null;
        }

        public async Task<IEnumerable<PfDocument>> GetTemplateFiles()
        {
            var getFileListApi = ConfigurationManager.AppSettings["PrintableFormsBaseUrl"] + 
                ConfigurationManager.AppSettings["PrintableFormsGetFileListApi"];
            var request = new HttpRequestMessage(HttpMethod.Get, getFileListApi);

            //var token = memoryCacheService.GetToken();

            //request.Headers.Add("Authorization", "Bearer " + token.AccessToken);

            var responseMessage = await SendRequest(request);
            string responseContent = string.Empty;

            if(responseMessage.IsSuccessStatusCode)
            {
                responseContent = await responseMessage.Content.ReadAsStringAsync();
            }
            
            return JsonConvert.DeserializeObject<List<PfDocument>>(responseContent);
        }

        private async Task<HttpResponseMessage> SendRequest(HttpRequestMessage request)
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
    }
}
