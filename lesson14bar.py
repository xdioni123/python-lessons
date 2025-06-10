import matplotlib.pyplot as plt

#Example data: Avarage IQ score by country

countries = ['Singapore', 'Honk Kong', 'South Korea', 'Japan', 'China', 'Switzerland','Netherlands','Germany', 'Kosova', 'Albania']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101, 93, 97]
colors = ["#4a6e10",'#952f8a','#61c02b','#bdd572','#0a9f03','#512d83','#ebab16','#eb16d8','#0390c5','#b91906']

#Create the bar chart
plt.figure(figsize=(10,6))
plt.bar(countries, iq_scores, color=colors)

plt.title("Avarage IQ by Country")
plt.xlabel("Country")
plt.ylabel("Avarage IQ Score")

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()