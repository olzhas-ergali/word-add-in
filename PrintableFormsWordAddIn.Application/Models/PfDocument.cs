using System;

namespace PrintableFormsWordAddIn.Application.Models
{
    public class PfDocument
    {
        public Guid DocumentId { get; set; }
        public string FileName { get; set; }
        public string Link { get; set; }
        public string ContentType { get; set; }
        public DateTime CreatedAt { get; set; }
        public string OrganizationName { get; set; }
    }
}
