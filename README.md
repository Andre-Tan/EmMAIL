# EmMAIL - Emm Automatic Isolate Labeller

EmMAIL is a command line tool for emm-type classification of Streptococcus pyogenes based on the isolate's whole genome sequence.

Input	: Assembled WGS reads of Streptococcus pyogenes

Output	: Predicted emm type of the isolate

The use of EmMAIL will follow the dependencies of the tools within its pipeline, namely BLAST and isPcr.

## Usage

EmMAIL has 2 branches of usage: direct BLAST, and isPcr followed with BLAST.
The arguments used in the pipeline are derived from the mentioned tools.

### BLAST Path
We directly use BLAST (specifically, blastn) against the assembled genome FASTA.
The required arguments are:
| Argument | Variable Type | Description |
| ------ | ------ | ------ |
| --query | FASTA | An assembled genome FASTA. Alignment will be checked within contigs; the longer the contigs, the better chance we have to find possible existing alignments |
| --db | blast DB | A BLAST database file |

Arguments for BLAST:
| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -dust | string | no | Filter query sequence with DUST |
| -perc_identity | integer | 95 | Minimal percent identity of sequence |
| -culling_limit | integer | 1 | Total hits to return in a single position |
| -outBLAST | filename | None | File to stream BLAST output to |
| -add_header | boolean | False | On mention, add header to BLAST output |

Arguments for BLAST filter:
| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -mismatch | integer | 4 | Threshold number of mismatch to allow in BLAST hit |
| -align_diff | integer | 5 | Threshold for difference between alignment length and subject length in BLAST hit |
| -gap | integer | 2 | Threshold number of gap to allow in BLAST hit |

### isPcr Path
We first extract targeted sequences using in silico PCR, and then BLAST the amplicons.
The required arguments are:
| Argument | Variable Type | Description |
| ------ | ------ | ------ |
| --primer | FASTA | A FASTA containing primer1 and primer2 as separate records |
| --query | FASTA | An assembled genome FASTA. Alignment will be checked within contigs; the longer the contigs, the better chance we have to find possible existing alignments |
| --db | blast DB | A BLAST database file |

Arguments for isPcr:
| Argument | Variable Type | Default | Description |
| ------ | ------ | ------ | ------ |
| -minPerfect | integer | 15 | Minimum size of perfect match at 3' primer end |
| -minGood | integer | 15 | Minimum size where there must be 2 matches for each mismatch. | 
| -minSize | integer | 0bps | Positive integer value for minimum product length | 
| -maxSize | integer | 4000bps | Positive integer value for maximum product length |
| -outPCR | filename | None (stdout) | A character string for if you want the amplicons sent to a file |
| -savePCR | boolean | False | On mention, PCR output file will not be automatically removed | 

Post-PCR, the arguments are the same as the ones in the BLAST path.

## Contact 

Should you want to fill issues or contact me about anything regarding EmMAIL, 
you can reach me here or on my email: andre.sutanto.91@gmail.com.