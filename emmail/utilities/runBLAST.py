from os import remove, environ
import logging

from emmail.objects.blast import BLAST
from emmail.objects.clusterer import Clusterer

from emmail.utilities import *

logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

def buildSubparser(parser):
    """
    Add arguments to the subparser, and return the subparser.
    """
    parser.usage = "emmail --query <QUERY>  --db <DB> [OPTIONS] blast [OPTIONS]"

    # BLAST options

    parser.add_argument("-dust", default="no", type=str,
                        help="Filter query sequence with DUST. Default no.")
    parser.add_argument("-perc_identity", default=perc_id_default, type=int,
                        help="Minimal percent identity of sequence. Default is {}.".format(perc_id_default))
    parser.add_argument("-culling_limit", default=culling_default, type=int,
                        help="Total hits to return in a position. Default is 5.".format(culling_default))

    # ResultRow options
    
    parser.add_argument("-mismatch", default=mismatch_default, type=int,
                        help="Threshold for number of mismatch to allow in BLAST hit. Default is {}.".format(mismatch_default))
    parser.add_argument("-align_diff", default=align_diff_default, type=int,
                        help="Threshold for difference between alignment length and subject length in BLAST hit. Default is {}.".format(align_diff_default))
    parser.add_argument("-gap", default=gap_default, type=int,
                        help="Threshold gap to allow in BLAST hit. Default is {}.".format(gap_default))
    
    return parser

def main(args):
    logger.info("Start running EmMAIL on {} queries.".format(len(args.query)))

    for i, query in enumerate(args.query):
    
        outBLAST = query.split("/")[-1].split(".")[0] + ".tmp"

        blast = BLAST(db = args.db, 
                        query = query, 
                        dust = args.dust, 
                        perc_identity = args.perc_identity,
                        culling_limit = args.culling_limit, 
                        
                        output_stream = outBLAST,
                        header = False,
                        
                        mismatch = args.mismatch,
                        align_diff = args.align_diff,
                        gap = args.gap)
                        
        blast.run_blastn_pipeline()

        clusterer = Clusterer(blastOutputFile=outBLAST,
                            distance = args.clust_distance,
                            output_stream=args.output_file,
                            output_type=args.output_type).main()
                            
        if not args.save_intermediary:
            remove(outBLAST)
            # logger.info("{} is removed from directory".format(outBLAST))
        
    logger.info("Finished EmMAIL.")