from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

import random

filmes = [
    "O Poderoso Chefão",
    "Um Sonho de Liberdade",
    "O Poderoso Chefão II",
    "Batman: O Cavaleiro das Trevas",
    "A Lista de Schindler",
    "O Senhor dos Anéis: O Retorno do Rei",
    "Pulp Fiction: Tempo de Violência",
    "Forrest Gump: O Contador de Histórias",
    "O Senhor dos Anéis: A Sociedade do Anel",
    "O Silêncio dos Inocentes",
    "Cidadão Kane",
    "O Rei Leão",
    "Titanic",
    "Guerra nas Estrelas",
    "De Volta para o Futuro",
    "Indiana Jones e os Caçadores da Arca Perdida",
    "Matrix",
    "Os Vingadores",
    "Jurassic Park: Parque dos Dinossauros",
    "Os Incríveis",
    "Procurando Nemo",
    "Toy Story",
    "Shrek",
    "Madagascar",
    "Kung Fu Panda",
    "A Era do Gelo",
    "Meu Malvado Favorito",
    "Carros",
    "Monstros S.A.",
    "Ratatouille",
    "Homem-Aranha",
    "Homem-Aranha 2",
    "Homem-Aranha 3",
    "Homem-Aranha: De Volta ao Lar",
    "Homem-Aranha: Longe de Casa",
    "Homem-Aranha: No Aranhaverso",
    "Homem-Aranha: Sem volta para Casa"
]   

racas_de_caes = [
    "Dachshund",
    "Husky Siberiano",
    "Malamute do Alasca",
    "Pastor Suíço",
    "Braco-da-transilvânia",
    "Sabujo colombiano",
    "American Bully",
    "Dogue de Bordeaux",
    "American Pit Bull Terrier",
    "Cão esquimó americano",
    "Manchester terrier",
    "Shar pei",
    "Coton de Tulear",
    "Cavalier King Charles Spaniel",
    "Buldogue Francês",
    "Poodle",
    "Chihuahua",
    "Akita Inu",
    "American staffordshire terrier",
    "Basenji",
    "Basset hound",
    "Beagle",
    "Bernese",
    "Vira-lata",
    "Shih Tzu",
    "Yorkshire",
    "Rottweiler",
    "Labrador Retriever",
    "Golden Retriever",
    "Boxer",
    "Bulldog Inglês",
    "Doberman",
    "Shiba Inu",
    "Pug",
    "Border Collie",
    "Pinscher",
    "Pit Bull",
    "Pinscher Miniatura",
    "Pinscher Alemão",
    "Corgi"
]

bandas = [
    "The Beatles",
    "Queen",
    "Led Zeppelin",
    "Pink Floyd",
    "Nirvana",
    "AC/DC",
    "The Rolling Stones",
    "The Who",
    "The Doors",
    "Guns N' Roses",
    "Metallica",
    "U2",
    "The Police",
    "The Cure",
    "The Clash",
    "The Smiths",
    "Charlie Brown Jr.",
    "Legião Urbana",
    "Raimundos",
    "O Rappa",
    "Engenheiros do Hawaii",
    "Capital Inicial",
    "Paralamas do Sucesso",
    "Titãs",
    "Barão Vermelho",
    "Soda Stereo",
    "Foo Fighters",
    "Red Hot Chili Peppers",
    "Pearl Jam",
    "Soundgarden",
    "Alice in Chains",
    "Black Sabbath",
    "Iron Maiden",
    "Judas Priest",
    "Ramones",
    "Deep Purple",
    "Kiss",
    "FLOW",
    "Asian Kung-Fu Generation",
    "NICO Touches the Walls",
    "SPYAIR"
]

carros = [
    "Gol",
    "Gol bolinha",
    "Gol quadrado",
    "Nissan GT-R",
    "Nissan 350Z",
    "Nissan 370Z",
    "Nissan Skyline",
    "Mazda RX-7",
    "Mazda RX-8",
    "Mazda MX-5",
    "Toyota Supra",
    "Toyota Celica",
    "Toyota GT86",
    "Ford Bronco",
    "Ford Mustang",
    "Ford Focus",
    "Chevrolet Camaro",
    "Chevrolet Camaro 1970",
    "Chevrolet Corvette",
    "Chevrolet Corvette C4",
    "Lamborghini Aventador",
    "Lamborghini Huracán",
    "Lamborghini Gallardo",
    "Lamborghini Countach",
    "Lamborghini Diablo",
    "Lamborghini Miura",
    "Lamborghini Murciélago",
    "Lamborghini Reventón",
    "Ferrari 458",
    "Ferrari 488",
    "Ferrari 599",
    "Ferrari 612",
    "Ferrari California",
    "Ferrari F12",
    "Ferrari F40",
    "Ferrari F50",
    "Ferrari LaFerrari",
    "Ferrari Testarossa",
    "Porsche 911",
    "Porsche 911 GT3",
    "Porsche 911 Turbo"
]

aves = [
    "Coruja-buraqueira",
    "Coruja-das-neves",
    "Coruja-do-mato",
    "Coruja-do-nabal",
    "Coruja-do-ártico",
    "Coruja-pequena",
    "Coruja-pintada",
    "Coruja-de-igreja",
    "Coruja-orelhuda",
    "Coruja-das-torres",
    "Coruja-calcária",
    "Coruja-das-torres",
    "Águia-chilena",
    "Águia-cobreira",
    "Águia-calcária",
    "Águia-cinzenta",
    "Águia-dourada",
    "Águia-imperial",
    "Águia-pesqueira",
    "Águia-pomarina",
    "Condor-andino",
    "Condor-californiano",
    "Condor-dos-andes",
    "Harpia",
    "Gavião-real",
    "Gavião-de-rabo-branco",
    "Gavião-de-rabo-branco",
    "Gavião-de-rabo-branco",
    "Pombo",
    "Bem-te-vi",
    "Papagaio"
]

mascotes = [
    "Louro José",
    "Xaropinho",
    "Baianinho das Casas Bahia",
    "Tony, o tigre",
    "Ronald McDonald",
    "Papa-burguer",
    "Mickey Mouse",
    "Mister Músculo",
    "Coelho do Nesquik",
    "Trakinas",
    "Canarinho Pistola",
    "Bibendum",
    "Chester Cheetah",
    "Coelho Duracell",
    "Kool-Aid Man",
    "Solzinho da Rihappy",
    "Dollynho",
    "Urso da Coca Cola",
    "Papai Noel Coca Cola",
    "Sansão",
    "Horácio",
    "Mario",
    "Sonic",
    "Pikachu",
    "Pernalonga",
    "Bob Esponja",
    "Gato da Toei Animation",
    "Gelatina Royal",
    "Pepsi Man",
    "Tio Patinhas",
    "Sackboy"
]

azul = [
    "azul",
    "azul marinho",
    "azul celeste",
    "azul turquesa",
    "azul royal",
    "azul petróleo",
    "azul bebê",
    "azul anil",
    "azul marinho",
    "azul cobalto",
    "azul safira",
    "azul tiffany",
    "azul piscina",
    "azul céu",
    "azul índigo",
    "azul ultramarino",
    "azul denim",
    "azul claro",
    "azul escuro",
    "azul violeta",
    "azul elétrico",
    "azul oceano",
    "azul gelo",
    "azul navy",
    "azul caneta",
    "azul da prússia",
    "azul aviador",
    "azul london",
    "azul klein",
    "azul metalizado",
    "azul normal",
]

vingadores = [
    "Homem de Ferro",
    "Capitão América",
    "Thor",
    "Hulk",
    "Viúva Negra",
    "Gavião Arqueiro",
    "Pantera Negra",
    "Doutor Estranho",
    "Homem-Formiga",
    "Feiticeira Escarlate",
    "Visão",
    "Soldado Invernal",
    "Falcão",
    "Máquina de Combate",
    "Nick Fury",
    "Maria Hill",
    "Phil Coulson",
    "Agente 13",
    "Mantis",
    "Nebulosa",
    "Gamora",
    "Drax",
    "Rocket",
    "Groot",
    "Star-Lord",
    "Thanos",
    "Loki",
    "Ultron",
    "Ronan",
    "Ego",
    "Caveira Vermelha",
    "Abominável",
    "Whiplash",
    "Mandarim",
    "Killmonger",
    "Vulture",
    "Hela",
    "Mysterio",
    "Taskmaster"
]



times = [
    "Flamengo",
    "Corinthians",
    "São Paulo",
    "Palmeiras",
    "Santos",
    "Vasco",
    "Botafogo",
    "Fluminense",
    "Grêmio",
    "Internacional",
    "Cruzeiro",
    "Atlético Mineiro",
    "Atlético Paranaense",
    "Coritiba",
    "Bahia",
    "Vitória",
    "Sport",
    "Santa Cruz",
    "Náutico",
    "Fortaleza",
    "Ceará",
    "Paysandu",
    "Remo",
    "Sampaio Corrêa",
    "Moto Club",
    "CSA",
    "CRB",
    "América Mineiro",
    "América Natal",
    "ABC",
    "Joinville"
]

capitais = [
    "Rio de Janeiro",
    "São Paulo",
    "Belo Horizonte",
    "Brasília",
    "Curitiba",
    "Florianópolis",
    "Porto Alegre",
    "Recife",
    "Salvador",
    "Fortaleza",
    "Natal",
    "João Pessoa",
    "Aracaju",
    "Maceió",
    "Teresina",
    "São Luís",
    "Belém",
    "Manaus",
    "Macapá",
    "Boa Vista",
    "Palmas",
    "Cuiabá",
    "Campo Grande",
    "Goiânia",
    "Vitória",
    "Rio Branco",
    "Porto Velho"
]

cidades = [
    "Londres",
    "Paris",
    "Nova York",
    "Tóquio",
    "Pequim",
    "Moscou",
    "Berlim",
    "Roma",
    "Madri",
    "Lisboa",
    "Atenas",
    "Amsterdã",
    "Viena",
    "Budapeste",
    "Varsóvia",
    "Praga",
    "Bruxelas",
    "Estocolmo",
    "Oslo",
    "Helsinque",
    "Copenhague",
    "Dublin",
    "Reykjavik",
    "Cidade do México",
    "Buenos Aires",
    "Santiago",
    "Lima",
    "Bogotá",
    "Caracas",
    "Quito",
    "La Paz"
]

personagens_de_jogos = [
    "Mario",
    "Luigi",
    "Peach",
    "Toad",
    "Yoshi",
    "Donkey Kong",
    "Diddy Kong",
    "Bowser",
    "Wario",
    "Link",
    "Zelda",
    "Ganondorf",
    "Samus",
    "Kirby",
    "Dante",
    "Kratos",
    "Nathan Drake",
    "Joel",
    "Ellie",
    "Master Chief",
    "Snake",
    "Sonic",
    "Tails",
    "Knuckles",
    "Shadow",
    "Dr. Robotnik",
    "CJ",
    "Tommy Vercetti",
    "Niko Bellic",
    "Doomslayer",
    "Doomguy"
]

jogos = [
    "Super Mario Bros.",
    "Ocarina of Time",
    "Majora's Mask",
    "Wind Waker",
    "Twilight Princess",
    "Skyward Sword",
    "Breath of the Wild",
    "Super Mario 64",
    "Mario Kart",
    "FINAL FANTASY VII",
    "God of War",
    "Uncharted",
    "The Last of Us",
    "Halo",
    "Metal Gear Solid",
    "Sonic the Hedgehog",
    "Grand Theft Auto",
    "DOOM"
    "Animal Crossing",
    "Valorant",
    "CS:GO",
    "Hotline Miami",
    "Among Us",
    "Minecraft",
    "The Sims",
    "League of Legends",
    "World of Warcraft",
    "Overwatch",
    "Fortnite",
    "Apex Legends",
    "Call of Duty"
]

marcas_de_carros = [
    "Ferrari",
    "Lamborghini",
    "Porsche",
    "Chevrolet",
    "Ford",
    "Nissan",
    "Toyota",
    "Audi",
    "BMW",
    "Mercedes-Benz",
    "Volkswagen",
    "Honda",
    "Hyundai",
    "Kia",
    "Mitsubishi",
    "Peugeot",
    "Renault",
    "Citroën",
    "Fiat",
    "Jeep",
    "Land Rover",
    "Volvo",
    "Jaguar",
    "Mini",
    "Subaru",
    "Suzuki",
    "Mazda",
    "Dodge",
    "Chrysler",
    "Buick",
    "Cadillac",
]
    
cafes = [
    "Café",
    "Café com leite",
    "Café expresso",
    "Café americano",
    "Café irlandês",
    "Café latte",
    "Café macchiato",
    "Café mocha",
    "Café turco",
    "Café vienense",
    "Café descafeinado",
    "Cappuccino",
    "Frappuccino",
    "Mocaccino",
    "Ristretto",
    "Affogato",
    "Flat White",
    "Irish Coffee",
    "Long Black",
    "Lungo",
    "Short Black",
    "Vienna Coffee",
    "Americano",
    "Café au lait",
    "Café bombón",
    "Café com chantilly",
    "Café com creme",
    "Café com especiarias",
    "Café com gelo",
    "Café com marshmallow",
]

hiragana = [
    "あ",
    "い",
    "う",
    "え",
    "お",
    "か",
    "き",
    "く",
    "け",
    "こ",
    "さ",
    "し",
    "す",
    "せ",
    "そ",
    "た",
    "ち",
    "つ",
    "て",
    "と",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ひ",
    "ふ",
    "へ",
    "ほ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "や",
    "ゆ",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "わ",
    "を",
    "ん",
]

katakana = [
    "ア",
    "イ",
    "ウ",
    "エ",
    "オ",
    "カ",
    "キ",
    "ク",
    "ケ",
    "コ",
    "サ",
    "シ",
    "ス",
    "セ",
    "ソ",
    "タ",
    "チ",
    "ツ",
    "テ",
    "ト",
    "ナ",
    "ニ",
    "ヌ",
    "ネ",
    "ノ",
    "ハ",
    "ヒ",
    "フ",
    "ヘ",
    "ホ",
    "マ",
    "ミ",
    "ム",
    "メ",
    "モ",
    "ヤ",
    "ユ",
    "ヨ",
    "ラ",
    "リ",
    "ル",
    "レ",
    "ロ",
    "ワ",
    "ヲ",
    "ン",
]

jump = [
    "Dragon Ball",
    "One Piece",
    "Naruto",
    "Bleach",
    "Boku no Hero Academia",
    "Jujutsu Kaisen",
    "Black Clover",
    "Demon Slayer",
    "Jojo Bizarre Adventure",
    "Toriko",
    "Hunter x Hunter",
    "Rurouni Kenshin",
    "Yu Yu Hakusho",
    "Shaman King",
    "Saint Seiya",
    "City Hunter",
    "Yugi-Oh",
    "Sakamoto Days",
    "Dr. Stone",
    "Death Note",
    "Haikyuu",
    "Slam Dunk",
    "Gintama",
    "Dragon Quest Dai no Daibouken",
    "Ao no Hako"
]

legends = [
    "Ronaldo Fenômeno",
    "Zinedine Zidane",
    "Ronaldinho Gaúcho",
    "Kaká",
    "Michael Owen",
    "Fabio Cannavaro",
    "Rivaldo",
    "Romário",
    "George Weah",
    "Paolo Rossi",
    "Lothar Matthäus",
    "Marco van Basten",
    "Michel Platini",
    "Diego Maradona",
    "Johan Cruyff",
    "Lev Yashin",
    "Pele",
    "Garrincha",
    "Zico",
    "Sócrates",
    "Rivellino",
    "Cafu",
    "Roberto Carlos",
    "Jairzinho",
    "Gabriel Batistuta",
    "Francesco Totti",
    "Alessandro Del Piero",
    "Andrea Pirlo",
    "Gianluigi Buffon",
    "Paolo Maldini",
    "Andres Iniesta",
    "Xavi",
    "Toni Kroos",
    "Thierry Henry",
    "David Beckham",
    "Steven Gerrard",
    "Frank Lampard",
    "Wayne Rooney",
    "Zlatan Ibrahimovic",
    "Luis Figo",
]

listas = [filmes, racas_de_caes, bandas, carros, aves, mascotes, azul, vingadores, times, capitais, cidades, 
personagens_de_jogos, jogos, marcas_de_carros, cafes, hiragana, katakana, jump, legends]

lista_tempo = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ranges = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29 ,30]

range_aleatorio = random.choice(ranges)

aleatorio = random.choice(listas)


mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Edge(options=edge_options)

execs = 1

for x in range(range_aleatorio):
    aleatorio = random.choice(listas)
    aleatorio_pesquisa = random.choice(aleatorio)
    aleatorio_tempo = random.choice(lista_tempo)
    driver.get('https://bing.com')
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
    element.send_keys(aleatorio_pesquisa)
    element.submit()
    
    time.sleep(aleatorio_tempo)

    execs+=1
driver.quit()