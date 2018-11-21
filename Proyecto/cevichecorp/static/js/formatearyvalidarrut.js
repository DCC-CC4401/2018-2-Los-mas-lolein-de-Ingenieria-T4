function formatRUT(rut)
{rut.value=rut.value.replace(/[.-]/g, '').replace( /^(\d{1,2})(\d{3})(\d{3})(\w{1})$/, '$1.$2.$3-$4')}