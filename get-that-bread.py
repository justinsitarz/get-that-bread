import pronouncing as pro

breads = ['Aish merahrah', 'Ajdov kruh', 'Anadama', 'Anpan', 'Appam', 'Hoppers', 'Arboud', 'Arepa', 'Baba', 'Bagel', 'Baguette', 'French stick', 'French', 
'Bakarkhani', 'Balep korkun', 'Bammy', 'Banana', 'Bannock', 'Bara Brith', 'Barbari', 'Barmbrack', 'Barm cake', 'Bastone', 'Italian stick', 'staff', 
'Bazin', 'Bazlama', 'Belgian waffle', 'Bhakri', 'Bialy', 'Bing', 'Biscotti', 'Biscuit', 'Black', 'Blaa', 'Bolani', 'Bolo do caco', 'Borlengo', 'Borodinsky', 
'Boule', 'Roll', 'Stick', 'Brioche', 'Brioche bun', 'Broa', 'Brown', 'Bublik', 'Canadian White', 'Carrot', 'Česnica', 'Challah', 'Chapati', 'Chickpea', 'Cholermüs', 
'Christmas wafer', 'Ciabatta', 'Coppia Ferrarese', 'Corn', 'Cottage loaf', 'Cozonac', 'Cracker', 'Crêpe', 'Crisp', 'Croutons', 'Crumpet', 'Cuban', 'Curry', 'Damper', 
'Dampfnudel', 'Dorayaki', 'Dosa', 'Eggette', 'English muffin', 'Farl', 'Filone', 'Flat', 'Flatbrød', 'Flatkaka', 'Focaccia', 'Fougasse', 'Green onion pancake', 
'Hallulla', 'Hardebrood', 'Hardtack', 'Himbasha', 'Hot and spicy cheese', 'Injera', 'Johnnycake, Hoecake', "Ka'ak", 'Kalach', 'Kamir', 'Kaya toast', 'Khanom bueang', 
'Khakhra', 'Khubz', 'Kifli', 'Kisra', 'Kitcha', 'Kulcha', 'Lagana', 'Lahoh', 'Lángos', 'Laobing', 'Lavash', 'Lefse', 'Lye roll', 'Malooga', 'Maltese', 'Ħobż tal-Malti', 
'Mantou', 'Markook', 'Marraqueta', 'Matzo', 'Melonpan', 'Miche', 'Michetta', 'Milk Loaf', 'Milk', 'Milk roll', 'Mollete', 'Mohnflesserl', 'Montreal-style bagel', 'Naan', 
'Ngome', 'Obwarzanek krakowski', "Pain d'épi", 'Wheat stalk', 'Pain de mie', 'Pancarré', 'Pan dulce', 'Panbrioche', 'Pandesal', 'Pandoro', 'Pane carasau', 
'Pane di Altamura', 'Pane ticinese', 'Panettone', 'Focaccia', 'Papadum, Papad', 'Paratha', 'Parotta', 'Barotta', 'Paximathia', 'Peg', 'Penia', 'Pita', 'Pizza', 
'Piadina', 'Pistolet', 'Pogača', 'Portuguese sweet', 'Potato', 'Potato pancake', 'Potbrood', 'Pretzel', 'Proja', 'Pumpernickel', 'Pumpkin', 'Puran Poli', 'Obbatu', 
'Bobbatlu', 'Bakshalu', 'Qistibi', 'Quick', 'Rewena', 'Rice', 'Rieska', 'Röggelchen', 'Roti', 'Roti bakar', 'Roti bolen', 'Roti buaya', 'Roti canai', 'Rugbrød', 
'Rumali Roti', 'Ryaninjun', 'Rye', 'Sacramental', 'Saj', 'Samoon', 'Salt-rising', 'Sangak', 'Scone', 'Sgabeo', 'Shirmal', 'Shokupan', 'Shoti', 'Soda', 'Sourdough', 
'Speckendick', 'Spelt', 'Sprouted', 'Taboon', 'Laffa', 'Taftan', 'Tandoor', 'Teacake', 'Texas toast', 'Tiger', 'Tortilla', 'Tsoureki', 'Ttongppang', 'Tunnbröd', 
'Uttappam', 'Vánočka', 'Vienna', 'White', 'Whole wheat', 'Yufka', 'Zopf', 'Zwieback', 'Babka', 'Bramboráček', 'Graham', 'Hard dough', 'Jewish rye', 'Khobz', 'Limpa', 
'Mischbrot', 'Pambazo', 'Sepik', 'Soboro', 'Telera', 'Toutons', 'Wagafi']

get_syns = ['get', 'attain', 'bag', 'nab', 'capture', 'clear', 'yield', 'obtain', 'pickup', 'grab', 'land', 'earn', 'secure', 'snag', 'wangle', 'bring in', 'glean', 
'hustle', 'fetch', 'acquire', 'access', 'win', 'come by', 'lock up', 'score', 'take', 'bring', 'draw', 'cop', 'procure', 'achieve', 'amass', 'buy', 'collect', 'gain', 
'get', 'have', 'pick up', 'promote', 'annex', 'catch', 'corral', 'gather', 'get hands on', 'get hold of', 'latch onto', 'rack up', 'scare up', 'take possession of']

def rhymeCheck(listA, listB):
	hype = set()

	listA_dict = {}
	for item in listA:
		last_word = item.split()[-1]
		listA_dict[item] = pro.rhymes(last_word)

	listB_dict = {}
	for item in listB:
		last_word = item.split()[-1]
		listB_dict[item] = pro.rhymes(last_word)

	for item in listA:
		last_word = item.split()[-1]
		lw_rhymes = pro.rhymes(last_word)
		for key, value in listB_dict.items():
			for lw in lw_rhymes:
				if lw in value:
					hype.add("Let's {} some {}".format(key, item))

	print(hype)



rhymeCheck(breads, get_syns)
