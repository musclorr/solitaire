ROUGE=2
BLANC=1
VIDE=0
boules = [ ROUGE, BLANC, BLANC, BLANC, BLANC, BLANC, VIDE, BLANC, BLANC, BLANC, BLANC, BLANC]

def bouleApres(i):
	"""
	Retourne la boule apres la boule numero i
	"""
	if i == 11:
		return 0
	else:
		return i+1


def bouleAvant(i):
	"""
	Retourne la boule avant la boule numero i
	"""
	if i == 0:
		return 11
	else:
		return i-1
		
def generate(config1):
	configs = []
	for i, boule in enumerate(config1):
		if boule == VIDE and config1[bouleAvant(i)] == BLANC and config1[bouleAvant(bouleAvant(i))] != VIDE:
			config2 = config1[:]
			config2[bouleAvant(bouleAvant(i))] = VIDE
			config2[bouleAvant(i)] = VIDE
			config2[i] = config1[bouleAvant(bouleAvant(i))]
			configs += [config2]
		if boule == VIDE and config1[bouleApres(i)] == BLANC and config1[bouleApres(bouleApres(i))] != VIDE:
			config2 = config1[:]
			config2[bouleApres(bouleApres(i))] = VIDE
			config2[bouleApres(i)] = VIDE
			config2[i] = config1[bouleApres(bouleApres(i))]
			configs += [config2]
	return configs
			
boules = [ ROUGE, BLANC, BLANC,VIDE, BLANC, BLANC,  BLANC, BLANC, BLANC, BLANC, BLANC, BLANC]		
configs = {1 : [boules] }
for i in range(1, 11):
	newconfigs = []
	for config0 in configs[i]:
		newconfigs += generate(config0)
	configs[i+1] = newconfigs

configs[11]
