import os
from typing import Literal

import librosa
import pandas as pd
import soundfile as sf


class Formatter:
    def process(self, 
                  transcript_dir: str,
                  audio_dir: str, 
                  recording_device: str,
                  topics: list[str], 
                  topics_endpointings: list[float],
                  environment: str,
                  language: str,
                  gender: Literal['M','F'],
                  speaker_name: str = 'S01',
                  end_timestamp_adder: float = 0.0
                  ):

        transcript_data = {}

        # Read the audio once
        y, sr = librosa.load(audio_dir, sr=None)

        audio_dir  = f'audio/{speaker_name}'
        metadata_dir  = 'metadata'
        annotation_dir  = 'annotation'
        os.makedirs(audio_dir , exist_ok=True)
        os.makedirs(metadata_dir , exist_ok=True)
        os.makedirs(annotation_dir , exist_ok=True)

        # Read the transcript
        with open(transcript_dir, "r") as f:
            content = f.read()

            for idx, line in enumerate(content.splitlines()):
                # Extract the data
                line_parts = line.strip().split()
                start_timestamp, end_timestamp, transcript = float(line_parts[0]), float(line_parts[1]) + end_timestamp_adder, " ".join(line_parts[2:])

                topic_idx = self._topic_helper(start_timestamp, topics_endpointings)
                topic_name = topics[topic_idx]
                duration = end_timestamp - start_timestamp
                filename = f"{speaker_name}_T{topic_idx+1:02d}_{idx:03d}.wav"

                transcript_data[filename] = {
                    'start': start_timestamp,
                    'end': end_timestamp,
                    'transcript': transcript,
                    'duration': duration,
                    'gender': gender,
                    'speaker': speaker_name,
                    'topic': topic_name,
                    'environment': environment,
                    'language': language,
                    'recording_device': recording_device
                }

                # Extract the audio and save
                curr_extracted_audio = y[int(start_timestamp * sr): int(end_timestamp * sr)]
                sf.write(f'audio/{speaker_name}/{filename}', curr_extracted_audio, sr)
                print(f"Saved track to audio/{speaker_name}/{filename}")

        self._metadata_to_csv(metadata_dir, transcript_data)
        self._annotation_to_csv(annotation_dir, transcript_data)

    def _topic_helper(self, curr_timestamp: float, topic_endpointings: list[float]):
        for idx in range(len(topic_endpointings) - 1, -1, -1):
            if curr_timestamp >= topic_endpointings[idx]:
                return idx
        return 0

    def _metadata_to_csv(self, metadata_dir, data: dict):
        filenames = data.keys()

        dataframe = pd.DataFrame({
            "File": filenames,
            "Speaker": [data[filename]['speaker'] for filename in filenames],
            "Gender": [data[filename]['gender'] for filename in filenames],
            "Language": [data[filename]['language'] for filename in filenames],
            "Topic": [data[filename]['topic'] for filename in filenames],
            "Duration": [data[filename]['duration'] for filename in filenames],
            "Environment": [data[filename]['environment'] for filename in filenames],
            "Device": [data[filename]['recording_device'] for filename in filenames],
            "Quality": ["to be examed" for _ in filenames],
            "Note": ["to be filled" for _ in filenames]
        })

        if os.path.exists(f"{metadata_dir}/metadata.csv"):
            print("Existing metadata detected")
            existing_csv = pd.read_csv(f"{metadata_dir}/metadata.csv")

            print("Adding new metada to existing metadata...")
            merged_csv = pd.concat([existing_csv, dataframe], axis=0, ignore_index=True)
            merged_csv.to_csv(f"{metadata_dir}/metadata.csv", index=False)
        else:
            dataframe.to_csv(f"{metadata_dir}/metadata.csv", index=False)

    def _annotation_to_csv(self, annotation_dir, data: dict):
        filenames = data.keys()

        dataframe = pd.DataFrame({
            "File": filenames,
            "Annotation": [data[filename]['transcript'] for filename in filenames],
        })

        if os.path.exists(f"{annotation_dir}/annotation.csv"):
            print("Existing annotation detected")
            existing_csv = pd.read_csv(f"{annotation_dir}/annotation.csv")

            print("Adding new annotation to existing annotation...")
            merged_csv = pd.concat([existing_csv, dataframe], axis=0, ignore_index=True)
            merged_csv.to_csv(f"{annotation_dir}/annotation.csv", index=False)
        else:
            dataframe.to_csv(f"{annotation_dir}/annotation.csv", index=False)


if __name__ == "__main__":
    formatter = Formatter()
    formatter.process(
        "daffa_transkrip.txt",
        "Daffa-Sunda-Audacity.wav",
        "Headphone",
        ["Rutinitas","Kenangan","Keresahan"],
        [0, 334.671000, 593.165562],
        "Indoor",
        "Sunda",
        "M",
        "S03",
        0.015
    )
    formatter.process(
        "mba_fatimah_transkrip.txt",
        "Mba-Fatimah-Sunda-Audacity.wav",
        "Headphone",
        ["Rutinitas","Kenangan","Keresahan"],
        [0, 413.229688, 634.397187],
        "Indoor",
        "Sunda",
        "F",
        "S04",
        0.015
    )