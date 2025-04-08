types = ['eq', 'reverbs', 'delays', 'compresores', 'limitadores', 'clippers', 'distorsiones', 'denoise', 'sintetizadores']

plugins_data = [
    # Ecualización
    ['eq', "ReaEQ", 'pagado'],           # Parte del paquete ReaPlugs de Cockos (gratuito, pero cerrado)
    ['eq', "TDR Nova", 'pagado'],          # Ecualizador dinámico (freeware, pero cerrado)
    ['eq', "Blue Cat's Triple EQ", 'pagado'],
    ['eq', "Voxengo Marvel GEQ", 'pagado'],
    ['eq', "Calf Equalizer", 'open source'],  # Disponible en Calf Studio Gear (usado en Linux)

    # Reverbs
    ['reverbs', "ValhallaRoom", 'pagado'],
    ['reverbs', "OrilRiver", 'pagado'],
    ['reverbs', "TAL-Reverb-4", 'pagado'],
    ['reverbs', "Dragonfly Reverb", 'open source'],  # Proyecto en GitHub con licencia abierta
    ['reverbs', "Freeverb3", 'open source'],         # Basado en el algoritmo Freeverb (versión abierta)

    # Delays
    ['delays', "ReaDelay", 'pagado'],                # ReaPlugs (gratuito, pero cerrado)
    ['delays', "TAL-Dub-3", 'pagado'],
    ['delays', "Voxengo Tempo Delay", 'pagado'],
    ['delays', "Blue Cat's Delay", 'pagado'],
    ['delays', "Dragonfly Delay", 'open source'],    # Parte de la colección Dragonfly (licencia open source)

    # Compresión
    ['compresores', "ReaComp", 'pagado'],             # Incluido en ReaPlugs
    ['compresores', "TDR Kotelnikov", 'pagado'],
    ['compresores', "DC1A", 'pagado'],                # Compresor freeware, pero código cerrado
    ['compresores', "Molot Compressor", 'pagado'],
    ['compresores', "Calf Compressor", 'open source'],

    # Limitadores
    ['limitadores', "ReaLimit", 'pagado'],           # Parte de ReaPlugs
    ['limitadores', "LoudMax", 'pagado'],
    ['limitadores', "Limiter No6", 'open source'],   # Se distribuye libremente con licencia abierta
    ['limitadores', "FabFilter Pro-L", 'pagado'],
    ['limitadores', "MLoudness", 'pagado'],          # De MeldaProduction (plugin comercial)

    # Clippers
    ['clippers', "Voxengo Overflow", 'pagado'],
    ['clippers', "SPL Clip", 'pagado'],
    ['clippers', "Airwindows XSat", 'open source'],  # Airwindows es conocido por su código abierto
    ['clippers', "ClipShifter", 'pagado'],
    ['clippers', "KClip", 'open source'],           # Ejemplo hipotético basado en proyectos open source

    # Distorsiones
    ['distorsiones', "Camel Crusher", 'pagado'],     # Plugin popular freeware (código cerrado)
    ['distorsiones', "Softube Saturation Knob", 'pagado'],
    ['distorsiones', "Krush", 'pagado'],             # Bitcrusher freeware (cerrado)
    ['distorsiones', "Guitarix Distortion", 'open source'],  # Parte de Guitarix (Linux, open source)
    ['distorsiones', "DC9 Distortion", 'pagado'],

    # Pitch (Pitch shifting)
    ['pitch', "PitchProof", 'pagado'],
    ['pitch', "MTransformer", 'pagado'],             # De MeldaProduction
    ['pitch', "Elastique Pitch", 'pagado'],
    ['pitch', "Little AlterBoy", 'pagado'],
    ['pitch', "SmbPitchShift", 'open source'],       # Basado en el algoritmo open source de Stephan Bernsee

    # Denoise
    ['denoise', "iZotope RX Elements", 'pagado'],
    ['denoise', "Waves WNS", 'pagado'],
    ['denoise', "ReaFIR", 'pagado'],                 # Usado en ReaPlugs en modo de noise reduction
    ['denoise', "Accusonus ERA Noise Remover", 'pagado'],
    ['denoise', "RNNoise VST", 'open source'],       # Basado en el proyecto RNNoise (libre en GitHub)

    # Sintetizadores
    ['sintetizadores', "Synth1", 'pagado'],          # Muy popular freeware (sin código abierto)
    ['sintetizadores', "Helm", 'open source'],         # Sintetizador gratuito y de código abierto
    ['sintetizadores', "ZynAddSubFX", 'open source'],  # Potente y de código abierto
    ['sintetizadores', "Dexed", 'open source'],        # Modelado del Yamaha DX7, open source
    ['sintetizadores', "TyrellN6", 'pagado']           # Gratuito, pero sin licencia open source (cerrado)
]
