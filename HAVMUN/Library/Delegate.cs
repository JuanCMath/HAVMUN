using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class Delegate : IDelegate
    {
        public ICountry _Country { get; }

        public IComission _Comission { get; }

        public string AccessCode { get; }

        public Delegate(ICountry country, IComission comission, string code)
        {
            _Country = country;
            _Comission = comission;
            AccessCode = code;
        }
    }
}
