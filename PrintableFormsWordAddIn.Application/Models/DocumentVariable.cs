using System;

namespace PrintableFormsWordAddIn.Application.Models
{
    public class DocumentVariable
    {
        public Guid Id { get; set; }
        public string Table { get; set; }
        public string Field { get; set; }
        public string Name { get; set; }
        public string Value { get; set; }
    }
}
