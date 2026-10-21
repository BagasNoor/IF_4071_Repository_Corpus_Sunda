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
## File Naming Convention

Audio files inside each speaker directory (`audio/S0X/`) follow a standardized naming structure:

S\{Speaker\_ID\}\_T\{Topic\_ID\}\_\{Index\}.wav

* **`S0X`**: Speaker Identifier (`S01` to `S10`)
* **`T0X`**: Topic Identifier
  * `T01`: Routines (daily activities)
  * `T02`: Memories (significant life experiences)
  * `T03`: Concerns (grievances or life struggles)
* **`Index`**: Sequential index of the clip for that speaker/topic combination (e.g., `001`, `002`)

*Example:* `S01_T02_005.wav` — Speaker 1, Topic 2 (Memories), 5th clip segment.

## Metadata & Annotation Schema

### 1. `annotation/annotation.csv`
Contains the target text for ASR training and evaluation.

| Column | Description | Example | 
| :--- | :--- | :--- |
| `File` | The filename  | `S01_T01_001.wav` |
| `Annotation` | Verbatim text transcription | *Abdi dinten ieu bade angkat ka kampus.* |

### 2. `metadata/metadata.csv`
Contains acoustic, demographic, and recording quality metadata across 10 fields.

| Field | Description | Example |
| :--- | :--- | :--- |
| `File` | Relative file path | `S01/S01_T01_001.wav` |
| `Speaker` | Speaker identifier | `S01` |
| `Gender` | Speaker gender | `Male` / `Female` |
| `Language` | Primary dialect/language | `Sundanese` |
| `Topic` | Conversation prompt category | `Routines` / `Memories` / `Concerns` |
| `Duration` | Clip duration in seconds | `4.52` |
| `Environment` | Recording location context | `Indoor` |
| `Device` | Recording hardware used | `USB Condenser Mic` / `Smartphone` |
| `Quality` | Quality control verification | `Good` / `Acceptable` / `Reject` |
| `Note` | Acoustic anomalies or notes | `Minor background fan noise` |

## Ethics & Consent
All audio recordings were collected with explicit, informed consent from participants. Signed consent forms are archived in documentation/consent/. The data is restricted to research and non-commercial educational purposes.
