using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class Votation : IVotation
    {
        public bool Open { get; private set; }

        public IComission _Comission { get; }

        public string Topic { get; }

        public List<IVote> Votes { get; }


        public Votation(IComission Comission, string topic)
        {
            _Comission = Comission;
            Topic = topic;
            Votes = new List<IVote>();
            Open = true;
        }

        public IVotationResult EndVotation()
        {
            int agree = 0;
            int against = 0;
            int abstention = 0;

            foreach (var vote in Votes)
            {
                switch (vote.Value)
                {
                    case VoteValue.Agree:
                        agree++;
                        break;
                    case VoteValue.Against:
                        against++;
                        break;
                    case VoteValue.Abstention:
                        abstention++;
                        break;
                }
            }

            Open = false;
            return new VotationResult(agree, against, abstention, agree * 100 / Votes.Count); //si se da en base al quorum, cambiar el dividendo por _Comission.Quorum
        }

        public void ReceiveVote(IVote vote) => Votes.Add(vote);
    }
}