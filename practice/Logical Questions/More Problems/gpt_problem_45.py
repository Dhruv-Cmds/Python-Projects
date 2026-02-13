# Create class Test:
# Use constructor like this:
# def __init__(harry, value):
#     harry.value = value
# Create object and print value.
# Then change harry to slf.
# Observe result.
# Answer (in your own words):
# Does the parameter name matter or only its position?

class Test:
    def __init__(slf, value):
        slf.value = value

t = Test(10)
print(t.value)