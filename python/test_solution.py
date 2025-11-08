import unittest
import yaml
import subprocess
import sys

class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('case.yaml', 'r', encoding='utf-8') as f:
            cls.test_cases = yaml.safe_load(f)

        print(f"\n{'=' * 60}")
        print(f"총 {len(cls.test_cases)}개의 테스트 케이스를 실행합니다.")
        print(f"{'=' * 60}\n")

    def test_all_cases(self):
        passed = 0
        failed = 0
        results = []

        for i, tc in enumerate(self.test_cases, 1):
            case_name = tc.get('name', f'Case {i}')

            result = subprocess.run(
                [sys.executable, 'solution.py'],
                input=tc['input'],
                capture_output=True,
                text=True,
                timeout=5
            )

            actual = result.stdout.strip()
            expected = tc['output'].strip()

            is_pass = actual == expected

            if is_pass:
                passed += 1
                print(f"✅ {case_name}: PASS")
            else:
                failed += 1
                print(f"❌ {case_name}: FAIL")

                results.append({
                    'name': case_name,
                    'input': tc['input'].strip(),
                    'expected': expected,
                    'actual': actual,
                    'stderr': result.stderr
                })

        print(f"\n{'=' * 60}")
        print(f"최종 결과: {passed}/{len(self.test_cases)} 통과")
        print(f"{'=' * 60}\n")

        if results:
            print("실패한 테스트 케이스 상세")
            print(f"{'=' * 60}")
            for r in results:
                print(f"\n[{r['name']}]\n")
                print(f"입력\n{r['input']}\n")
                print(f"기대값\n{r['expected']}\n")
                print(f"실제값\n{r['actual']}\n")

                if r['stderr']:
                    print(f"에러\n{r['stderr']}")

                print(f"{'-' * 60}\n")

            self.fail(f"{failed}개 테스트 실패")

if __name__ == '__main__':
    unittest.main(verbosity=2)