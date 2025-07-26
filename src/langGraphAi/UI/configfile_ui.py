from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langGraphAi/UI/configfile_ui.ini"):
        # to read the configfile_ui.ini
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config["default"].get("page_title").split(", ")
    
    def get_llm_options(self):
        return self.config["default"].get("llm_options").split(", ")
    
    def get_usecase_options(self):
        return self.config["default"].get('usecase_options').split(", ")
    
    def get_groq_model_options(self):
        return self.config["default"].get('groq_model_options').split(", ")
    


