from deduce import Deduce

version="DeduceConf"
version_path="/home/tom/deduce/configs"


def initialize_deduce(load_base_config=False,config=f"{version_path}/{version}/aumc_config.json",build_lookup_structs=False):

    model = Deduce()

    # override standard, bit better for html rendering
    model.processors["post_processing"]["redactor"].open_char = "["
    model.processors["post_processing"]["redactor"].close_char = "]"

    return model
