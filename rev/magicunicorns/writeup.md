# Magic Unicorns

I denne challengen får vi fila magic. Den spør deg først om et navn og så en registreringsnøkkel. I programmet ser vi 7 funksjoner av interesse: 
a(), b(), c(), d(), e(), f() og main().

Når vi skriver inn navnet, kjøres den gjennom e() og dersom man debugger, kan man lese av verdien e() returnerer. 
Logikken i e() var ganske komplisert, men ikke nødvendig å forstå for å løse oppgaven. 

Videre hentes det inn 49 tall. Disse tallen blir formatert i en 7x7-matrise som det gjøres en del sjekker på. 

Disse tallen kjøres først gjennom a(). Her sjekkes det om summen av hver rad er like verdien e() returnerte. 

```__int64 __fastcall a(__int64 a1, unsigned int a2)
{
  int i; // [rsp+14h] [rbp-Ch]
  int v4; // [rsp+18h] [rbp-8h]
  int j; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i <= 6; ++i )
  {
    v4 = 0;
    for ( j = 0; j <= 6; ++j )
      v4 += *(_DWORD *)(a1 + 28LL * i + 4LL * j);
    if ( v4 != a2 )
      return 0LL;
  }
  return b(a1, a2);
}```

Dersom dette stemmer, sendes tallene til b().
b() sjekker om summen av hver kolonne er lik ouputten fra e(). Dersom de er det, sendes de videre til c()

```__int64 __fastcall b(__int64 a1, unsigned int a2)
{
  int i; // [rsp+14h] [rbp-Ch]
  int v4; // [rsp+18h] [rbp-8h]
  int j; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i <= 6; ++i )
  {
    v4 = 0;
    for ( j = 0; j <= 6; ++j )
      v4 += *(_DWORD *)(a1 + 28LL * j + 4LL * i);
    if ( v4 != a2 )
      return 0LL;
  }
  return c(a1, a2);
}```

I c() gjøres en sjekk på summen i diagonalen som starter starter i siste kolonne i første rad. Her skal også summen være lik outputten fra e()

```__int64 __fastcall c(__int64 a1, int a2)
{
  int v3; // [rsp+14h] [rbp-Ch]
  int v4; // [rsp+18h] [rbp-8h]
  int v5; // [rsp+1Ch] [rbp-4h]

  v3 = 0;
  v4 = 0;
  v5 = 6;
  while ( v4 <= 6 )
    v3 += *(_DWORD *)(a1 + 28LL * v4++ + 4LL * v5--);
  if ( v3 == a2 )
    return d(a1, a2);
  else
    return 0LL;
}```

d() gjør det samme som c(), men sjekker den andre diagonalen

```__int64 __fastcall d(__int64 a1, int a2)
{
  int v3; // [rsp+14h] [rbp-Ch]
  int v4; // [rsp+18h] [rbp-8h]
  int v5; // [rsp+1Ch] [rbp-4h]

  v3 = 0;
  v4 = 0;
  v5 = 0;
  while ( v4 <= 6 )
    v3 += *(_DWORD *)(a1 + 28LL * v4++ + 4LL * v5++);
  if ( v3 == a2 )
    return f(a1);
  else
    return 0LL;
}```

Til slutt sjekkes det om noen av verdiene i diagonalen som begynner øverst til venstre har like tall langs kolonna eller raden. 

```__int64 __fastcall f(__int64 a1)
{
  int i; // [rsp+8h] [rbp-10h]
  int j; // [rsp+Ch] [rbp-Ch]
  int k; // [rsp+10h] [rbp-8h]

  for ( i = 0; i <= 6; ++i )
  {
    for ( j = 0; j <= 6; ++j )
    {
      if ( j != i && *(_DWORD *)(a1 + 28LL * i + 4LL * i) == *(_DWORD *)(a1 + 28LL * j + 4LL * i) )
        return 0LL;
    }
    for ( k = i + 1; k <= 6; ++k )
    {
      if ( k != i && *(_DWORD *)(a1 + 28LL * i + 4LL * i) == *(_DWORD *)(a1 + 28LL * i + 4LL * k) )
        return 0LL;
    }
  }
  return 1LL;
}```

Dersom f() returnerer 1, får vi tilsendt flagget.

For å løse dette, fant jeg en streng jeg benyttet som navn hver ang jeg kjørte programmet, slik at ouputten fra e() ble konstant. Deretter fant jeg syv ulike tall som summet opp til verdien fra e().

Til slutt lekte jeg litt med tallen, og fikk en matrise som kom gjennom alle sjekkene.

```send = [[1480, 1500, 1400, 1450, 1460, 1761, 1310],
        [1400, 1450, 1460, 1761, 1310, 1480, 1500],
        [1460, 1761, 1310, 1480, 1500, 1400, 1450],
        [1310, 1480, 1500, 1400, 1450, 1460, 1761],
        [1500, 1400, 1450, 1460, 1761, 1310, 1480],
        [1450, 1460, 1761, 1310, 1480, 1500, 1400],
        [1761, 1310, 1480, 1500, 1400, 1450, 1460],
]```

## EPT{y0u_ar3_a_m4g1c4l_un1c0rn!}