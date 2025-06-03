using Newtonsoft.Json;

namespace PrintableFormsWordAddIn.Application.Models
{
    public class KeyCloakError
    {
        [JsonProperty("error")]
        public string Error { get; set; }
        [JsonProperty("error_description")]
        public string ErrorDescription { get; set; }
    }
}
