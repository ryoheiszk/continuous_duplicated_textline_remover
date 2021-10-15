import os
import shutil
import sys


def main(log_path, extension):
    files = [file for file in os.listdir(log_path) if os.path.splitext(file)[1] == "." + extension]

    for file in files:
        with open(os.path.join(log_path, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) > 50000:
                print("行数が多すぎるため分割してください。")
                return False
            print(f"{file}を開きました。")

            # 最後の要素に改行コードがない場合は付与しておく。
            if not lines[-1] in "\n":
                lines[-1] += "\n"

        lines_new = []
        for j, line in enumerate(lines):
            # 1行目だけ特別な処理をする。
            if j == 0:
                lines_new.append(line)

            if line == lines[j-1]:
                print(f"[{j+1}/{len(lines)}]重複した行を検出しました。")
                continue
            else:
                lines_new.append(line)

        with open(os.path.join(output_dir, file), "w", encoding="utf-8") as f:
            f.writelines(lines_new)
            print(f"{file}を保存しました。")


if __name__ == "__main__":
    log_path = sys.argv[1]
    extension = input("対象の拡張子を入力してください。(例: txt): ")

    output_dir = os.path.join(log_path, "outputs")

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
        print("既製の出力フォルダが確認されたため、削除しました。")

    os.makedirs(output_dir)

    main(log_path, extension)

    import subprocess
    subprocess.call('PAUSE', shell=True)
