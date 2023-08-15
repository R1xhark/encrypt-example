# Šifrování Souborů pomocí AES v režimu CFB8

Tento skript umožňuje šifrovat soubory pomocí symetrického šifrování AES v režimu CFB8. Je důležité poznamenat, že toto je pouze jednoduchý příklad a nemělo by to být považováno za komplexní nástroj pro hodnocení zabezpečení dat.

## Použití

1. Nejdříve si stáhněte tento skript a umístěte ho do adresáře, kde máte soubory, které chcete šifrovat.
2. Otevřete příkazový řádek a přejděte do adresáře kde máte skript uložen.

```cd cesta/k/adresari```
   
Spusťte skript pomocí následujícího příkazu:

```python nazev_skriptu.py```

Skript vás vyzve, abyste zadali název souboru, který chcete zašifrovat, a heslo pro šifrování.

Po zadání názvu souboru a hesla skript provede šifrování obsahu souboru a vytvoří nový zašifrovaný soubor.

## Závislosti

Tento skript využívá knihovnu cryptography, kterou můžete nainstalovat pomocí následujícího příkazu:

```pip install cryptography```

### Důležité Upozornění

Tento skript je pouze ukázkovým příkladem šifrování dat. Skutečná ochrana dat vyžaduje komplexní bezpečnostní opatření, jako je správná správa klíčů, zabezpečení hesel, síťová bezpečnost a další aspekty. Před použitím tohoto skriptu nebo jeho modifikací v produkčním prostředí doporučujeme provést detailní analýzu zabezpečení.

### Licence

Tento skript je poskytován pod licencí MIT. Více informací najdete v souboru LICENSE.

### pozn: decryption.py zvrati efekt encryption.py pro desifrovani dat
