all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(x):
	return x["sexy"]==True
l=list(filter(filter_colors, all_colors))
def generate_li(x):
	return "<li>"+x["label"]+"</li>"
ll=list(map(generate_li, l))
t=""
for k in ll:
	t=t+k
print(t)