import random
lname = [
"Smith",
"Johnson",
"Williams",
"Brown",
"Jones",
"Miller",
"Davis",
"Garcia",
"Rodriguez",
"Wilson",
"Martinez",
"Anderson",
"Taylor",
"Thomas",
"Hernandez",
"Moore",
"Martin",
"Jackson",
"Thompson",
"White",
"Lopez",
"Lee",
"Gonzalez",
"Harris",
"Clark",
"Lewis",
"Robinson",
"Walker",
"Perez",
"Hall",
"Young",
"Allen",
"Sanchez",
"Wright",
"King",
"Scott",
"Green",
"Baker",
"Adams",
"Nelson",
"Hill",
"Ramirez",
"Campbell",
"Mitchell",
"Roberts",
"Carter",
"Phillips",
"Evans",
"Turner",
"Torres",
"Parker",
"Collins",
"Edwards",
"Stewart",
"Flores",
"Morris",
"Nguyen",
"Murphy",
"Rivera",
"Cook",
"Rogers",
"Morgan",
"Peterson",
"Cooper",
"Reed",
"Bailey",
"Bell",
"Gomez",
"Kelly",
"Howard",
"Ward",
"Cox",
"Diaz",
"Richardson",
"Wood",
"Watson",
"Brooks",
"Bennett",
"Gray",
"James",
"Reyes",
"Cruz",
"Hughes",
"Price",
"Myers",
"Long",
"Foster",
"Sanders",
"Ross",
"Morales",
"Powell",
"Sullivan",
"Russell",
"Ortiz",
"Jenkins",
"Gutierrez",
"Perry",
"Butler",
"Barnes",
"Fisher",
"Henderson",
"Coleman",
"Simmons",
"Patterson",
"Jordan",
"Reynolds",
"Hamilton",
"Graham",
"Kim",
"Gonzales",
"Alexander",
"Ramos",
"Wallace",
"Griffin",
"West",
"Cole",
"Hayes",
"Chavez",
"Gibson",
"Bryant",
"Ellis",
"Stevens",
"Murray",
"Ford",
"Marshall",
"Owens",
"Mcdonald",
"Harrison",
"Ruiz",
"Kennedy",
"Wells",
"Alvarez",
"Woods",
"Mendoza",
"Castillo",
"Olson",
"Webb",
"Washington",
"Tucker",
"Freeman",
"Burns",
"Henry",
"Vasquez",
"Snyder",
"Simpson",
"Crawford",
"Jimenez",
"Porter",
"Mason",
"Shaw",
"Gordon",
"Wagner",
"Hunter",
"Romero",
"Hicks",
"Dixon",
"Hunt",
"Palmer",
"Robertson",
"Black",
"Holmes",
"Stone",
"Meyer",
"Boyd",
"Mills",
"Warren",
"Fox",
"Rose",
"Rice",
"Moreno",
"Schmidt",
"Patel",
"Ferguson",
"Nichols",
"Herrera",
"Medina",
"Ryan",
"Fernandez",
"Weaver",
"Daniels",
"Stephens",
"Gardner",
"Payne",
"Kelley",
"Dunn",
"Pierce",
"Arnold",
"Tran",
"Spencer",
"Peters",
"Hawkins",
"Grant",
"Hansen",
"Castro",
"Hoffman",
"Hart",
"Elliott",
"Cunningham",
"Knight"]
gname = ["Mary",
"Anna",
"Emma",
"Elizabeth",
"Minnie",
"Margaret",
"Ida",
"Alice",
"Bertha",
"Sarah",
"Annie",
"Clara",
"Ella",
"Florence",
"Cora",
"Martha",
"Laura",
"Nellie",
"Grace",
"Carrie",
"Maude",
"Mabel",
"Bessie",
"Jennie",
"Gertrude",
"Julia",
"Hattie",
"Edith",
"Mattie",
"Rose",
"Catherine",
"Lillian",
"Ada",
"Lillie",
"Helen",
"Jessie",
"Louise",
"Ethel",
"Lula",
"Myrtle",
"Eva",
"Frances",
"Lena",
"Lucy",
"Edna",
"Maggie",
"Pearl",
"Daisy",
"Fannie",
"Josephine",
"Dora",
"Rosa",
"Katherine",
"Agnes",
"Marie",
"Nora",
"May",
"Mamie",
"Blanche",
"Stella",
"Ellen",
"Nancy",
"Effie",
"Sallie",
"Nettie",
"Della",
"Lizzie",
"Flora",
"Susie",
"Maud",
"Mae",
"Etta",
"Harriet",
"Sadie",
"Caroline",
"Katie",
"Lydia",
"Elsie",
"Kate",
"Susan",
"Mollie",
"Alma",
"Addie",
"Georgia",
"Eliza",
"Lulu",
"Nannie",
"Lottie",
"Amanda",
"Belle",
"Charlotte",
"Rebecca",
"Ruth",
"Viola",
"Olive",
"Amelia",
"Hannah",
"Jane",
"Virginia",
"Emily",
"Matilda",
"Irene",
"Kathryn",
"Esther",
"Willie",
"Henrietta",
"Ollie",
"Amy",
"Rachel",
"Sara",
"Estella",
"Theresa",
"Augusta",
"Ora",
"Pauline",
"Josie",
"Lola",
"Sophia",
"Leona",
"Anne",
"Mildred",
"Ann",
"Beulah",
"Callie",
"Lou",
"Delia",
"Eleanor",
"Barbara",
"Iva",
"Louisa",
"Maria",
"Mayme",
"Evelyn",
"Estelle",
"Nina",
"Betty",
"Marion",
"Bettie",
"Dorothy",
"Luella",
"Inez",
"Lela",
"Rosie",
"Allie",
"Millie",
"Janie",
"Cornelia",
"Victoria",
"Ruby",
"Winifred",
"Alta",
"Celia",
"Christine",
"Beatrice",
"Birdie",
"Harriett",
"Mable",
"Myra",
"Sophie",
"Tillie",
"Isabel",
"Sylvia",
"Carolyn",
"Isabelle",
"Leila",
"Sally",
"Ina",
"Essie",
"Bertie",
"Nell",
"Alberta",
"Katharine",
"Lora",
"Rena",
"Mina",
"Rhoda",
"Mathilda",
"Abbie",
"Eula",
"Dollie",
"Hettie",
"Eunice",
"Fanny",
"Ola",
"Lenora",
"Adelaide",
"Christina",
"Lelia",
"Nelle",
"Sue",
"Johanna",
"Lilly",
"Lucinda",
"Minerva",
"Lettie",
"Roxie",
"Cynthia",
"Helena",
"Hilda",
"Hulda"]
bname = ["John",
"William",
"James",
"Charles",
"George",
"Frank",
"Joseph",
"Thomas",
"Henry",
"Robert",
"Edward",
"Harry",
"Walter",
"Arthur",
"Fred",
"Albert",
"Samuel",
"David",
"Louis",
"Joe",
"Charlie",
"Clarence",
"Richard",
"Andrew",
"Daniel",
"Ernest",
"Will",
"Jesse",
"Oscar",
"Lewis",
"Peter",
"Benjamin",
"Frederick",
"Willie",
"Alfred",
"Sam",
"Roy",
"Herbert",
"Jacob",
"Tom",
"Elmer",
"Carl",
"Lee",
"Howard",
"Martin",
"Michael",
"Bert",
"Herman",
"Jim",
"Francis",
"Harvey",
"Earl",
"Eugene",
"Ralph",
"Ed",
"Claude",
"Edwin",
"Ben",
"Charley",
"Paul",
"Edgar",
"Isaac",
"Otto",
"Luther",
"Lawrence",
"Ira",
"Patrick",
"Guy",
"Oliver",
"Theodore",
"Hugh",
"Clyde",
"Alexander",
"August",
"Floyd",
"Homer",
"Jack",
"Leonard",
"Horace",
"Marion",
"Philip",
"Allen",
"Archie",
"Stephen",
"Chester",
"Willis",
"Raymond",
"Rufus",
"Warren",
"Jessie",
"Milton",
"Alex",
"Leo",
"Julius",
"Ray",
"Sidney",
"Bernard",
"Dan",
"Jerry",
"Calvin",
"Perry",
"Dave",
"Anthony",
"Eddie",
"Amos",
"Dennis",
"Clifford",
"Leroy",
"Wesley",
"Alonzo",
"Garfield",
"Franklin",
"Emil",
"Leon",
"Nathan",
"Harold",
"Matthew",
"Levi",
"Moses",
"Everett",
"Lester",
"Winfield",
"Adam",
"Lloyd",
"Mack",
"Fredrick",
"Jay",
"Jess",
"Melvin",
"Noah",
"Aaron",
"Alvin",
"Norman",
"Gilbert",
"Elijah",
"Victor",
"Gus",
"Nelson",
"Jasper",
"Silas",
"Christopher",
"Jake",
"Mike",
"Percy",
"Adolph",
"Maurice",
"Cornelius",
"Felix",
"Reuben",
"Wallace",
"Claud",
"Roscoe",
"Sylvester",
"Earnest",
"Hiram",
"Otis",
"Simon",
"Willard",
"Irvin",
"Mark",
"Jose",
"Wilbur",
"Abraham",
"Virgil",
"Clinton",
"Elbert",
"Leslie",
"Marshall",
"Owen",
"Wiley",
"Anton",
"Morris",
"Manuel",
"Phillip",
"Augustus",
"Emmett",
"Eli",
"Nicholas",
"Wilson",
"Alva",
"Harley",
"Newton",
"Timothy",
"Marvin",
"Ross",
"Curtis",
"Edmund",
"Jeff",
"Elias",
"Harrison",
"Stanley",
"Columbus",
"Lon",
"Ora",
"Ollie",
"Russell",
"Pearl",
"Solomon",
"Arch",
"Asa"]
def randomname(n, l):
	n2 = random.choice(n)
	l2 = random.choice(l)
	name = "{} {}".format(n2, l2)
	return name
def randomnames(a):
	choice = random.randrange(0, 2)
	if choice == 0:
		for i in range(0, a):
		    print(randomname(bname, lname))
	if choice == 1:
		for i in range(0, a):
		    print(randomname(gname, lname))
