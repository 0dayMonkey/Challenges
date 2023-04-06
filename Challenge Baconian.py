ciphertext = "bacoN's CIPheR Or THe BACOniAN CiphEr is a mEtHoD of stegAnogrApHY (A mETHod of hiDIng a SecrEt MESsaGE As opposed To a TrUe ciPheR) dEviSed bY FrANCiS bACon. A meSsAGE iS ConcEALeD in THE pRESentATioN of TeXT, RAtHeR than itS cONtEnt. to enCOde a meSsaGE, eAch leTTEr oF ThE PlAINTexT is rEplaceD bY a grOup Of fIve OF ThE LEttErs 'A' or 'B'. tHis REPlACEmenT Is DONe aCCOrdinG TO the AlpHaBEt of The BACoNian ciPhEr, sHoWn beloW. nOTE: A sECONd vErSiOn oF BaCoN'S CiPhEr uSeS A UnIqUe cOdE FoR EaCh lEtTeR. iN OtHeR WoRdS, i aNd j eAcH HaS ItS OwN PaTtErN. tHe wRiTeR MuSt mAkE UsE Of tWo dIfFeReNt tYpEfAcEs fOr tHiS CiPhEr. AfTeR PrEpArInG A FaLsE MeSsAgE WiTh tHe sAmE NuMbEr oF LeTtErS As aLl oF ThE As aNd bS In tHe rEaL, sEcReT MeSsAgE, tWo tYpEfAcEs aRe cHoSeN, oNe tO RePrEsEnT As aNd tHe oThEr bS. tHeN EaCh lEtTeR Of tHe fAlSe mEsSaGe mUsT Be pReSeNtEd iN ThE ApPrOpRiAtE TyPeFaCe, AcCoRdInG To wHeThEr iT StAnDs fOr aN A Or a b. To dEcOdE ThE MeSsAgE, tHe rEvErSe mEtHoD Is aPpLiEd. EaCh 'TyPeFaCe 1' LeTtEr iN ThE FaLsE MeSsAgE Is rEpLaCeD WiTh aN A AnD EaCh 'TyPeFaCe 2' LeTtEr iS RePlAcEd wItH A B. tHe bAcOnIaN AlPhAbEt iS ThEn uSeD To rEcOvEr tHe oRiGiNaL MeSsAgE. aNy mEtHoD Of wRiTiNg tHe mEsSaGe tHaT AlLoWs tWo dIsTiNcT RePrEsEnTaTiOnS FoR EaCh cHaRaCtEr cAn bE UsEd fOr tHe bAcOn cIpHeR. bAcOn hImSeLf pRePaReD A BiLiTeRaL AlPhAbEt[2] FoR HaNdWrItTeN CaPiTaL AnD SmAlL LeTtErS WiTh eAcH HaViNg tWo aLtErNaTiVe fOrMs, OnE To bE UsEd aS A AnD ThE OtHeR As b. ThIs wAs pUbLiShEd aS An iLlUsTrAtEd pLaTe iN HiS De aUgMeNtIs sCiEnTiArUm (ThE AdVaNcEmEnT Of lEaRnInG). BeCaUsE AnY MeSsAgE Of tHe rIgHt lEnGtH CaN Be uSeD To cArRy tHe eNcOdInG, tHe sEcReT MeSsAgE Is eFfEcTiVeLy hIdDeN In pLaIn sIgHt. ThE FaLsE MeSsAgE CaN Be oN AnY ToPiC AnD ThUs cAn dIsTrAcT A PeRsOn sEeKiNg tO FiNd tHe rEaL MeSsAgE."
bacon_dict = {'AAAAA':'a', 'AAAAB':'b', 'AAABA':'c', 'AAABB':'d', 'AABAA':'e', 'AABAB':'f', 'AABBA':'g', 'AABBB':'h', 'ABAAA':'i', 'ABAAB':'j', 'ABABA':'k', 'ABABB':'l', 'ABBAA':'m', 'ABBAB':'n', 'ABBBA':'o', 'ABBBB':'p', 'BAAAA':'q', 'BAAAB':'r', 'BAABA':'s', 'BAABB':'t', 'BABAA':'u', 'BABAB':'v', 'BABBA':'w', 'BABBB':' ', 'BBAAA':'y', 'BBAAB':'z'}

bacon_seq = ""
for c in ciphertext:
    if c.isalpha():
        if c.isupper():
            bacon_seq += "B"
        else:
            bacon_seq += "A"

text = ""
for i in range(0, len(bacon_seq), 5):
    code = bacon_seq[i:i+5]
    if code in bacon_dict:
        text += bacon_dict[code]
    else:
        text += code

print(text)
