# write your code here
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple

[x.unlink() for x in Path(__file__).parent.glob('*.txt')]


@dataclass
class Leerling:
    voornaam: str
    achternaam: str
    score_physics: int
    score_chemistry: int
    score_math: int
    score_engineering: int
    score_toelatingsexamen: int
    keuze1: str
    keuze2: str
    keuze3: str

    final_score: float = None

    def __post_init__(self):
        # for k, v in vars(self).items():
        #     if k.startswith('score_'):
        #         setattr(self, k, int(v))

        self.score_physics = int(self.score_physics)
        self.score_chemistry = int(self.score_chemistry)
        self.score_math = int(self.score_math)
        self.score_engineering = int(self.score_engineering)
        self.score_toelatingsexamen = int(self.score_toelatingsexamen)


def vul_de_klas(applicants: List[Leerling], de_klas: list, wat_doe_ik_graag: str, keuze: str) -> None:
    to_delete = []

    for ll in applicants:
        mijn_keuze = getattr(ll, keuze)
        if mijn_keuze == wat_doe_ik_graag and len(de_klas) != N:
            de_klas.append(ll)
            to_delete.append(ll)

    for ll in to_delete:
        applicants.remove(ll)


def sorted_list(applicants, wat_doe_ik_graag):
    def sort_how(ll: Leerling) -> Tuple[float, str, str]:
        if wat_doe_ik_graag == "Physics":
            mean = (ll.score_physics + ll.score_math) / 2

        elif wat_doe_ik_graag == "Chemistry":
            mean = ll.score_chemistry

        elif wat_doe_ik_graag == "Mathematics":
            mean = ll.score_math

        elif wat_doe_ik_graag == "Engineering":
            mean = (ll.score_engineering + ll.score_math) / 2

        elif wat_doe_ik_graag == "Biotech":
            mean = (ll.score_chemistry + ll.score_physics) / 2

        else:
            raise ValueError(f"Don't know {wat_doe_ik_graag}")

        ll.final_score = max(mean, ll.score_toelatingsexamen)

        return -ll.final_score, ll.voornaam, ll.achternaam

    return sorted(applicants, reverse=False, key=sort_how)


N = int(input())
names_plus_score = []

f = Path("applicants.txt")
if f.exists():
    applicants = f.read_text()
else:
    applicants = """Jermine Brunton 84 81 73 92 48 Physics Engineering Mathematics
Justo Mirfin 71 77 61 60 41 Engineering Biotech Chemistry
Uzma Naysmythe 60 94 75 71 80 Chemistry Engineering Mathematics
Koury Wingo 71 81 81 83 59 Engineering Biotech Mathematics
Kentrell Hillhouse 40 69 42 58 20 Mathematics Engineering Biotech
Trica Macalpine 75 80 96 88 66 Engineering Mathematics Biotech
Sang Muldoon 84 92 80 60 79 Physics Mathematics Engineering
Laney Braithwaite 90 90 90 72 94 Physics Chemistry Mathematics
Spring Burridge 71 84 98 71 50 Mathematics Chemistry Engineering
Delta Fanny 84 85 83 86 49 Chemistry Physics Mathematics
Elen Ashbury 54 76 88 62 60 Mathematics Chemistry Biotech
Ruthanne Scaife 75 73 84 97 82 Engineering Biotech Mathematics
Jaemi Hallets 81 71 73 86 78 Physics Engineering Mathematics
Artavious Fay 71 77 61 60 61 Engineering Biotech Chemistry
Franki Dinnis 60 94 75 71 80 Chemistry Biotech Mathematics
Marlynn Favell 71 81 81 93 79 Engineering Biotech Mathematics
Sameera Procter-Baines 70 59 72 68 80 Mathematics Engineering Biotech
Shantale Tompkins 75 80 96 88 66 Engineering Mathematics Biotech
Cornellius Turney 84 92 80 60 79 Physics Mathematics Engineering
Blia Sagar 90 81 80 72 94 Physics Chemistry Biotech
Wynn Crampton 71 84 98 71 50 Mathematics Chemistry Engineering
Linda Risley 85 85 83 86 49 Chemistry Physics Mathematics
Divina Butterworth 54 76 88 62 70 Mathematics Chemistry Biotech
Meshell Otway-Ruthven 75 73 84 97 94 Engineering Biotech Mathematics
Ammon Janssen 84 81 73 92 48 Physics Engineering Mathematics
Maila Greg 71 77 61 60 49 Mathematics Biotech Chemistry
Madiha Milligan 60 94 79 71 80 Physics Engineering Chemistry
Humphrey Spakeman 71 81 81 83 89 Chemistry Biotech Mathematics
Marygrace Wheelton 60 77 42 55 60 Mathematics Engineering Biotech
Takyra Sieminski 74 80 96 92 66 Engineering Mathematics Physics
Jathan Birley 84 92 80 60 79 Physics Mathematics Engineering
Tawnia Alcock 81 80 90 72 91 Biotech Chemistry Physics
Quinisha Clarkson 71 84 98 71 80 Mathematics Chemistry Engineering
Dashanna Herron 80 85 73 86 89 Physics Chemistry Mathematics
Verlon Mcconnell 84 61 88 62 60 Mathematics Chemistry Biotech
Tawsha Rodgers 78 71 84 97 82 Engineering Biotech Mathematics
Derick Whatley 81 91 73 80 78 Physics Engineering Mathematics
Tisheena Mckenney 76 57 61 90 61 Engineering Physics Biotech
Kyona Catrol 60 94 75 77 40 Chemistry Biotech Mathematics
Jamarl Delap 92 81 85 93 79 Engineering Biotech Mathematics
Tulio Carloss 66 59 82 64 60 Mathematics Engineering Physics
Kaylie Lanthis 75 80 96 88 66 Engineering Mathematics Biotech
Martha Hatchard 84 92 80 60 79 Physics Mathematics Engineering
Genee Mccrae 90 81 80 72 94 Biotech Chemistry Physics
Luna Pheobe 71 84 98 71 50 Chemistry Mathematics Engineering
Savvas Hjellstrom 55 85 41 66 45 Chemistry Biotech Mathematics
Mehul Bull 94 76 88 61 70 Mathematics Physics Biotech
Kennedy Barrett 77 93 84 87 94 Chemistry Biotech Mathematics
Marquita Mcrae 84 81 73 92 48 Physics Engineering Biotech
Natha Keefe 71 67 53 60 31 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 80 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 59 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 40 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 38 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 59 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 44 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 72 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 50 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 30 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 22 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 78 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 41 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 80 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 75 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 80 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 36 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 79 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 81 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 21 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 69 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 70 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 94 Physics Biotech Engineering
Elroy Leyte 84 81 73 92 48 Engineering Physics Mathematics
Jessye Allum 71 77 61 60 49 Mathematics Biotech Chemistry
Pearl Pullins 60 94 79 71 33 Chemistry Engineering Mathematics
Brittania Denny 90 84 70 61 72 Chemistry Physics Mathematics
Mendy Macmillan 61 81 81 70 51 Biotech Engineering Mathematics
Ramina Ogilvie 80 65 70 68 29 Mathematics Engineering Biotech
Ronel Cowan 75 80 96 88 66 Engineering Mathematics Biotech
Stacey Revill 84 92 84 70 51 Chemistry Physics Mathematics
Mir Ashley 71 84 98 71 83 Mathematics Physics Chemistry
Ayeshia Jackman 80 85 73 86 89 Chemistry Physics Mathematics
Jordann Rives 84 61 88 62 60 Mathematics Chemistry Biotech
Katrine Proby 78 71 84 90 42 Engineering Biotech Mathematics
Jermain Stobbs 81 91 73 80 78 Physics Engineering Mathematics
Sharief Macallister 76 57 61 99 61 Engineering Physics Biotech
Shannette Cowie 60 94 75 77 20 Chemistry Biotech Mathematics
Melena Hearn 92 81 85 93 79 Engineering Biotech Mathematics
Moraima Kendell 66 59 82 64 60 Mathematics Engineering Physics
Amira Giddings 75 80 96 78 66 Engineering Mathematics Physics
Tyrone Fern 64 92 80 52 79 Physics Mathematics Engineering
Joaquin Mytton 54 76 88 62 60 Mathematics Chemistry Biotech
Ehab Cocciardi 75 73 84 97 82 Engineering Biotech Mathematics
Tamkia Fish 81 71 73 86 78 Physics Engineering Mathematics
Deniz Blanchard 71 77 61 60 61 Engineering Biotech Chemistry
Mira Riley 60 94 75 71 80 Chemistry Biotech Mathematics
Loura Macansh 71 81 81 93 79 Engineering Physics Mathematics
Nastassja Trustram 60 49 82 68 70 Mathematics Engineering Physics"""

applicants = applicants.splitlines()
applicants = [Leerling(*applicant.split()) for applicant in applicants]

klassen = defaultdict(list)
alle_vakken = sorted(['Biotech', 'Engineering', 'Physics', 'Mathematics', 'Chemistry'])
for i in range(3):
    for vak in alle_vakken:
        applicants = sorted_list(applicants, vak)
        vul_de_klas(applicants, klassen[vak], vak, f'keuze{i+1}')

for departement, leerlingen in klassen.items():
    with open(f"{departement.lower()}.txt", "w") as f:
        for ll in sorted_list(leerlingen, departement):
            f.writelines(f"{ll.voornaam} {ll.achternaam} {ll.final_score:.1f}\n")
