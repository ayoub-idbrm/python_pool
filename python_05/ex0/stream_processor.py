from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and all(
                isinstance(x, (int, float))
                for x in data
            )
        )

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")
            total = sum(data)
            avg = total / len(data)
            return (
                f"Processed {len(data)} numeric values, "
                f"sum={total}, avg={avg}"
            )
        except Exception as e:
            return f"Numeric processing error: {e}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (isinstance(data, str))

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            word = data.split()
            return f"Processed text: {len(data)} characters, {len(word)} words"
        except Exception as a:
            return f"Text processing error: {a}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (isinstance(data, str) and ':' in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")
            lvl, dataa = data.split(":", 1)
            return f"[ALERT] {lvl} level detected: {dataa}"
        except Exception as d:
            return f"log processing error: {d}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num = [1, 2, 3, 4, 5]
    print(f"Processing data: {num}")
    print("Validation: Numeric data verified")
    pro = NumericProcessor()
    res = pro.process(num)
    print(pro.format_output(res))
    print()

    print("Initializing Text Processor...")
    text = "Hello Nexus World"
    tex = TextProcessor()
    print(f"Processing data: {text}")
    print("Validation: Text data verified")
    result = tex.process(text)
    print(tex.format_output(result))
    print()

    print("Initializing Log Processor...")
    log = LogProcessor()
    loog = "ERROR: Connection timeout"
    print(f'Processing data: "{loog}"')
    print("Validation: Log entry verified")
    ress = log.process(loog)
    print(log.format_output(ress))
    print()

    print("=== Polymorphic Processing Demo ===\n")
    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready"
    ]

    i = 0
    for proc, dat in zip(processors, data):
        res = proc.process(dat)
        i += 1
        print(f"Result {i}: {res}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
