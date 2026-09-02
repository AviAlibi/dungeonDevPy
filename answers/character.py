class Character:
	def __init__(
		self,
		name: str,
		maxHealth: float = 100.00,
		damageMultiplier: float = 1.00,
		attackPower: float = 10.00,
		defense: float = 1.00,
	) -> None:
		self.name = name
		self.maxhealth = maxHealth if maxHealth > 0 else 1
		self.health = self.maxhealth
		self.damageMultiplier = damageMultiplier
		self.attackPower = attackPower
		self.defense = defense

	def takeDamage(self, num: float) -> float:
		damageToInflict = num * self.defense
		damageToInflict = 0 if damageToInflict <= 0 else damageToInflict
		self.health -= damageToInflict
		return damageToInflict

	def heal(self, num: float) -> float:
		if num > 0:
			self.health += num
		self.health = self.maxhealth if self.health > self.maxhealth else self.health
		return self.health

	def isAlive(self):
		return self.health > 0

	def calculateDamage(self) -> float:
		return self.attackPower * self.damageMultiplier

	def attack(self, target: "Character") -> float:
		damage = self.calculateDamage()
		damageTaken = target.takeDamage(damage)
		return damageTaken

	def __str__(self) -> str:
		return f"{self.name} | HP: {self.health:.1f}/{self.maxhealth:.1f} | ATK: {self.attackPower} | DEF: {self.defense}"
