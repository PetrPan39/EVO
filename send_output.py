plugin_name = "send_output"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: send_output"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.send_output(*args, **kwargs)
