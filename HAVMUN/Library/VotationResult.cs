using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class VotationResult : IVotationResult
    {
        public int Agree { get; }

        public int Against { get; }

        public int Abstention { get; }

        public float PercentOfAproval { get; }

        public VotationResult(int agree, int against, int abstention, float percentOfAproval)
        {
            Agree = agree;
            Against = against;
            Abstention = abstention;
            PercentOfAproval = percentOfAproval;
        }
    }
}
