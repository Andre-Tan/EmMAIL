from os import path, environ
import logging
import subprocess

from emmail.objects.command import Command, FileNotInPathException

logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

class IsPCR(Command):

    def __init__(self, assembly_filename, primer_filename, min_perfect, min_good,
                max_product_length, output_stream):
                
        Command.__init__(self, "isPcr")
        
        self.assembly_filename = Command.assert_filepath_and_return(assembly_filename)
        self.primer_filename = Command.assert_filepath_and_return(primer_filename)
        
        self.min_perfect = min_perfect
        self.min_good = min_good
        
        self.max_product_length = max_product_length
        self.output_stream = output_stream
        
        self.command_string = self.build_isPCR_command()
    
    def __repr__(self):
        return self.command_string
    
    def build_isPCR_command(self):
            
        string = ("isPcr {db} {query} {output} "
                    "-minPerfect={} -minGood={} "
                    "-maxSize={}")
        
        command = string.format(self.min_perfect,
                                self.min_good,
                                self.max_product_length,
                                db=self.assembly_filename, 
                                query=self.primer_filename, 
                                output=self.output_stream)
        
        return command
    
    def run_isPCR(self):
        # logger.info("Running on {}".format(self.assembly_filename))
        
        output = Command.run(self)
        
        if not output:
            logger.info("There is no output for {}".format(self.assembly_filename))
        
        return output[:-1]