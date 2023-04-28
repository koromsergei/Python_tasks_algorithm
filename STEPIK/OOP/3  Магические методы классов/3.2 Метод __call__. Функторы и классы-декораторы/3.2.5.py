class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        value = args[0]
        try:
            int(value)
            return int(value)
        except ValueError:
            return None


lst = ['123', 's', 'sd', '24']
dr = DigitRetrieve()
print(list(map(dr, lst)))
