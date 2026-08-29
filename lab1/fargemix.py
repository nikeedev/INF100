colA = int(input("Grunnfarge:\n"))
colB = int(input("Målfarge:\n"))
ratio = float(input("Andel målfarge:\n"))

colA_red = colA % 1_000_000_000 // 1_000_000
colA_green = colA % 1_000_000 // 1_000
colA_blue = colA % 1_000

colB_red = colB % 1_000_000_000 // 1_000_000
colB_green = colB % 1_000_000 // 1_000
colB_blue = colB % 1_000

diff_red = round(colA_red + ((colB_red - colA_red) * ratio)) * 1_000_000
diff_green = round(colA_green + ((colB_green - colA_green) * ratio)) * 1_000
diff_blue = round(colA_blue + ((colB_blue - colA_blue) * ratio))

print(int(diff_red + diff_green + diff_blue))

