using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class Secretary : ISecretary
    {
        public IComission _Comission { get; }

        public string AccessCode { get; }

        public Secretary(IComission Comission, string accessCode)
        {
            _Comission = Comission;
            AccessCode = accessCode;
        }
    }
}
