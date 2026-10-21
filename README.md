# IF_4071_Repository_Corpus_Sunda

## Description
This repository serves as a corpus for creating ASR system that specifically handles the Sundanese language. The repository is also part of IF4071 (Speech Processing) lecture from Institut Technology of Bandung where students are instructed to prepare their own corpus using a predefined procedure to create a high quality, well documented, and ethically collected data. The corpus 

## Corpus Specification
|Aspect        | Specifications               |
|--------------|------------------------|
| Language          | Sundanese                 | 
| Number of Speakers          | 10 invdividuals              | 
| Gender          | 5 Male + 5 Female         |
| Type of Speech          | Spontaneuous Speech/Script Reading  |
| Speaker Type          | Native & Non-Native    |
| Topics          | Routines (daily activities), Memories (significant life experiences), Concerns (grievances or life struggles)    | 
| Duration          | ± 10-15 minutes per speaker   |  
| Sampling Rate          | 16 kHz   |
| Bit Depth          | 16-bit   |
| Channel          | Mono   |
| Format          | .wav   |
| Environment          | Indoor, relatively quiet   |
| Metadata          | Included   |
| Quality Control          | Good, Acceptable, Reject   |
| Annotation          | Transcription, Labels   |

## Repository Structure
  ```bash
      .
      ├── annotation/
      │ └── annotation.csv
      ├── audio/
      │ ├── S01
      │ ├── S02
      │ ├── S03
      │ ├── S04
      │ ├── S05
      │ ├── S06
      │ ├── S07
      │ ├── S08
      │ ├── S09
      │ └── S10
      ├── documentation/
      │ ├── documents
      │ └── consent
      ├── metadata/
      │ └── metadata.csv
      ├── utils/
      │ └── utils.py
      ├── .python-version 
      ├── README.md
      ├── pyproject.toml 
      └── uv.lock
  ```
