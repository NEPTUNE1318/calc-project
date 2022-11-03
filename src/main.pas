PROGRAM Part10;
VAR
    number     : INTEGER;
    a, b, c, x : INTEGER;
    z          : REAL;
BEGIN
    BEGIN
        number := 3;
        a := number;
        b := 10 * a + 10 * number DIV 4;
        c := a - - b
    END;
    x := 11;
    z := 20 / 7 + 3.14;
END.
