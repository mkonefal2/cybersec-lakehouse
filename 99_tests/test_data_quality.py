from pathlib import Path
import importlib.util


def load_generator():
    module_path = Path(__file__).resolve().parents[1] / '00_setup' / '01_generate_sample_data.py'
    spec = importlib.util.spec_from_file_location('gen', module_path)
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    return gen


def test_firewall_data_generation():
    gen = load_generator()
    df = gen.generate_firewall_logs(10)
    assert 'Source Port' in df.columns
    assert len(df) == 10
