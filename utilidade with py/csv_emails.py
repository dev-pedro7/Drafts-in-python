# Realizado para alteração em massa nos grupos do Google admin
import csv

group_email = "g.grupo@empresa.com.br"  # Substitua pelo e-mail do grupo real
member_type = "USER"
member_role = "MEMBER"

emails = [
    # Lista de E-mails
]

with open("membros_grupo.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Group Email [Required]", "Member Email", "Member Type", "Member Role"])
    for email in emails:
        writer.writerow([group_email, email, member_type, member_role])

print("Arquivo 'membros_grupo.csv' criado com sucesso!")
