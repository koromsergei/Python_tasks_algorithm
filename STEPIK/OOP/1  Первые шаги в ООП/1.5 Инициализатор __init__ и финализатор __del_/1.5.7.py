class CPUCheck:
    def __init__(self, name: str, fr: int):
        self.name = name
        self.fr = fr


class MemoryCheck:
    def __init__(self, name: str, volume):
        self.name = name
        self.volume = volume


class MotherBoardCheck:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.mem_slots = args
        self.total_mem_slots = len(self.mem_slots)

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'ЦП: {self.cpu.name}',
                f'Cлоты памяти: {self.total_mem_slots}',
                f'Память: ' + "; ".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]


mb = MotherBoardCheck('Mother1', CPUCheck('cpu1', 12000), MemoryCheck('mom1', 8), MemoryCheck('mom2', 8), MemoryCheck('mom3', 16))
print(mb.get_config())
