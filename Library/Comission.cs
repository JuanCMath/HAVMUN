using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class Comission : IComission
    {
        public int Number { get; }

        public int Quorum => Delegates.Count;

        public List<IDelegate> Delegates { get; }

        public ISecretary Secretary { get; }

        public Comission(int number, List<IDelegate> delegates, ISecretary secretary)
        {
            Number = number;
            Delegates = delegates;
            Secretary = secretary;
        }
    }
}
