using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library
{
    class Country : ICountry
    {
        public string Name { get; }
        public Country(string name) => Name = name;
    }
}
