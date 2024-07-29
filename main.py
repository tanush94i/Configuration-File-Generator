import yaml
import os
import logging

def generate_config(template_file, output_file):
    """Generates a configuration file from a YAML template.

    Args:
        template_file: Path to the YAML template file.
        output_file: Path to the output configuration file.
    """

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    try:
        with open(template_file, 'r') as f:
            config_data = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Template file '{template_file}' not found.")
        return
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        return

    try:
        with open(output_file, 'w') as f:
            for key, value in config_data.items():
                f.write(f"{key}: {value}\n")
        logger.info(f"Configuration file generated successfully: {output_file}")
    except OSError as e:
        logger.error(f"Error writing to output file: {e}")
        return

if __name__ == "__main__":
    template_file = 'config.yaml'
    output_file = 'generated_config.txt'
    generate_config(template_file, output_file)
