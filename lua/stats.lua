function mean(dataset)
    return sum(dataset) / len(dataset)
end


data = {}
length = 5
for i=1,length do
    data[i] = io.read()
end